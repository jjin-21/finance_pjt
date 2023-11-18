from django.shortcuts import render
import urllib.request
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import json

# Create your views here.
client_id = "CYv34EtcXhZ6vin_mvaa"
client_secret = settings.NAVER_API_KEY
base_url = "https://openapi.naver.com/v1/search/news.json?query="

@api_view(['GET'])
def deposit(request):
    encText = urllib.parse.quote("예금 상품")
    url = base_url + encText # JSON 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        return Response(json.loads(response_body.decode('utf-8')), status=status.HTTP_200_OK)
    else:
        return Response({"message": "조회에 실패했습니다."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def saving(request):
    encText = urllib.parse.quote("적금 상품")
    url = base_url + encText # JSON 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        return Response(json.loads(response_body.decode('utf-8')), status=status.HTTP_200_OK)
    else:
        return Response({"message": "조회에 실패했습니다."}, status=status.HTTP_404_NOT_FOUND)
