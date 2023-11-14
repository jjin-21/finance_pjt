from django.urls import path
from . import views

app_name = 'finances'
urlpatterns = [
    path('save-products/', views.save_products, name='save_products'),
    path('deposit-products/', views.deposit_products, name='deposit_products'),
    path('saving-products/', views.saving_products, name='saving_products'),
    path('deposit-product-options/<str:fin_prdt_cd>/', views.deposit_product_options, name='deposit_product_options'),
    path('saving-product-options/<str:fin_prdt_cd>/', views.saving_product_options, name='saving_product_options'),
    # path('finance-products/', views.finance_products, name='finance_products'),
    # path('finance-product-options/<str:fin_prdt_cd>/', views.finance_product_options, name='finance_product_options'),
    # path('finance-products/top_rate/', views.top_rate, name='top_rate'),
]
