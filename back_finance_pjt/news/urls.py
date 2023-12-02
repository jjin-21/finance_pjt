from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('deposit/', views.deposit),
    path('saving/', views.saving),
]
