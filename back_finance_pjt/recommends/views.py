from django.shortcuts import render
import joblib
import pandas as pd
from accounts.models import User
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from collections import Counter
import sklearn


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
    print(recommend_list)
    return Response({"message": "Good"})
# age	money	salary	gender
