from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from datetime import datetime

from .models import ExchangeRate
from .serializers import ExchangeRateSerializer
# Create your views here.

# 환율 저장
@api_view(['GET'])
def save(request):
    if request.method == "GET":
        # now = datetime.now()
        # formatted_date = now.strftime("%Y%m%d")
        URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
        params = {
            'authkey': settings.RATE_API_KEY,
            'searchdate': 20231123,
            'data': 'AP01'
        }

        response = requests.get(URL, params=params).json()
        # ExchangeRate.objects.all().delete()
        print(response)
        rate_data =ExchangeRate.objects.all()
        # print(bool(rate_data))
        if rate_data:
            rate_data.delete()
            
        for info in response:

            if "," in info["deal_bas_r"]:
                info["deal_bas_r"] = info["deal_bas_r"].replace(",","")
                info["tts"] = info["tts"].replace(",","")
                info["ttb"] = info["ttb"].replace(",","")
            serializer = ExchangeRateSerializer(data=info)
            if serializer.is_valid():
                serializer.save()
        return Response({'message': "Good!"}, status=status.HTTP_201_CREATED)


# 환율 조회
@api_view(['GET'])
def calculator(request):
    if request.method == 'GET':
        products = ExchangeRate.objects.all()
        serializer = ExchangeRateSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)