from django.shortcuts import render
import joblib
import pandas as pd
from accounts.models import User
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from collections import Counter
import sklearn
from finances.models import DepositProducts, SavingProducts

deposit_products = ['WR0001B', '00320342', '10511008000996000', '10511008001004000', 
                    '10511008001166004', '10511008001278000', '01030500510002', '01030500560002', 
                    '01030500600002', 'TD11300027000', 'TD11300031000', 'TD11300035000', 'TD11300036000', 
                    '200000301', '200000303', '10-01-20-024-0046-0000', '10-01-20-024-0059-0000', '21001115', 
                    '21001203', '01211310121', '01211310127', '01211310130', '05100', '06492', '010300100335', 
                    '200-0135-12', '10-003-1225-0001', '10-003-1381-0001', '10-003-1384-0001', '10-003-1387-0001', 
                    '4', '01013000110000000001', '10120110400011', '10120114300011', '10120114700011', '10120116100011', 
                    '10-01-20-388-0002', '1001202000002']

saving_products = ['WR0001F', 'WR0001L', '00266451', '10521001000846001', '10521001001177000', '10527001000925000', 
                    '10527001001272000', '10527001001278000', '01020400380001', '01020400490001', '01020400490002', 
                    '01020400510001', '01020400530001', '01020400610001', 'TD11330029000', 'TD11330030000', 'TD11330031000', 
                    'TD11330032000', '220002101', '220002301', '220002501', '220002701', '10-01-30-031-0018-0000', '10-01-30-031-0037-0000', 
                    '21000111', '21001116', '21001199', '21001236', '21001259', '01211210110', '01211210113', '01211210121', '01211210122', 
                    '03010', '03100', '03202', '010200100051', '010200100092', '010200100104', '230-0119-85', '10-047-1360-0002', 
                    '10-047-1365-0001', '10-047-1381-0001', '10-047-1387-0001', '10-059-1264-0001', '52', '53', '01012000200000000003', 
                    '01012000210000000000', '10140110400011', '10140114300011', '10140114700031', '10141109800021', '10141114300011', 
                    '10141114700031', '10141116600001', '10-01-30-355-0002', '10-01-30-355-0005', '1001303001001', '1001303001003', 
                    '1001303001004', '1001303001005']


# Create your views here.
@api_view(['GET'])
def recommend(request, user_pk):
    a = pd.read_csv('recommends/data.csv')
    loaded_kmeans = joblib.load('recommends/finance_model.pkl')
    user = User.objects.get(pk=user_pk)
    user_df = pd.DataFrame([[user.age, user.asset, user.salary, user.gender]],
                            columns=['age', 'gender', 'money', 'salary'])
    # DataFrame을 사용하여 예측 수행
    predictions = loaded_kmeans.predict(user_df)

    a['cluster'] = loaded_kmeans.labels_

    # # 동일한 클러스터에 있는 사용자의 금융 상품 추출
    financial_products = a.loc[a['cluster'] == predictions[0], 'product']

    # # 상품별 개수 계산
    product_count = dict(Counter(','.join(financial_products).split(';')))

    # # 개수별로 제품 정렬
    sorted_products = sorted(product_count.items(), key=lambda x: x[1], reverse=True)

    # # 추천상품 표시
    recommend_list = []
    for product, count in sorted_products[:6 ]:
        if product != '':
            recommend_list.append(product)
    deposit_recommends = []
    saving_recommends = []
    for recommend in recommend_list:
        if recommend in deposit_products:
            tmp = DepositProducts.objects.get(fin_prdt_cd=recommend)
            deposit_recommends.append({'kor_co_nm': tmp.kor_co_nm,
                                        'fin_prdt_cd': tmp.fin_prdt_cd,
                                        'fin_prdt_nm': tmp.fin_prdt_nm,
                                    })
        elif recommend in saving_products:
            tmp = SavingProducts.objects.get(fin_prdt_cd=recommend)
            saving_recommends.append({'kor_co_nm': tmp.kor_co_nm,
                                        'fin_prdt_cd': tmp.fin_prdt_cd,
                                        'fin_prdt_nm': tmp.fin_prdt_nm,
                                    })
    print("Deposit",deposit_recommends)
    print("Saving",saving_recommends)
    return Response({
        "deposit_recommends": deposit_recommends,
        "saving_recommends": saving_recommends
    })