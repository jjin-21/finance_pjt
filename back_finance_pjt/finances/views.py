from django.shortcuts import render, redirect
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

from .models import DepositOptions, DepositProducts, SavingOptions, SavingProducts
from .serializers import DepositOptionsSerializer, DepositProductsSerializer, SavingProductsSerializer, SavingOptionsSerializer

# Create your views here.
# 상품 저장
@api_view(['GET'])
def save_products(request):
    BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'
    # Deposits_list = ['depositProductsSearch.json', 'savingProductsSearch.json']
    # 예금 상품
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
    'auth': settings.API_KEY,
    'topFinGrpNo': '020000',
    'pageNo': 1
    }
    result = []
    response = requests.get(URL, params=params).json()
    res_data = response['result']
    baseList = res_data['baseList']
    optionList = res_data['optionList']

    # baseList
    for base in baseList:
        serializer = DepositProductsSerializer(data=base)
        if serializer.is_valid():
            serializer.save()
            result.append(serializer)
    # optionList
    for option in optionList:
        product = DepositProducts.objects.get(fin_prdt_cd=option['fin_prdt_cd'])
        serializer = DepositOptionsSerializer(data=option)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)
            result.append(serializer)
    
    # 적금 상품
    URL = BASE_URL + 'savingProductsSearch.json'
    params = {
    'auth': settings.API_KEY,
    'topFinGrpNo': '020000',
    'pageNo': 1
    }
    result = []
    response = requests.get(URL, params=params).json()
    res_data = response['result']
    baseList = res_data['baseList']
    optionList = res_data['optionList']

    # baseList
    for base in baseList:
        serializer = SavingProductsSerializer(data=base)
        if serializer.is_valid():
            serializer.save()
            result.append(serializer)
    # optionList
    for option in optionList:
        product = SavingProducts.objects.get(fin_prdt_cd=option['fin_prdt_cd'])
        serializer = SavingOptionsSerializer(data=option)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)
            result.append(serializer)
    return Response({'message': "Good!"}, status=status.HTTP_201_CREATED)


# 예금 상품 조회
@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 적금 상품 조화
@api_view(['GET', 'POST'])
def saving_products(request):
    if request.method == 'GET':
        products = SavingProducts.objects.all()
        serializer = SavingProductsSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = SavingProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 예금 옵션 조회
@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    print('Hello')
    options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(options, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 적금 옵션 조회
@api_view(['GET'])
def saving_product_options(request, fin_prdt_cd):
    options = SavingOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = SavingOptionsSerializer(options, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
