from django.urls import path
from . import views

app_name = "consultings"
urlpatterns = [
    path('', views.consulting_list),
    path('<int:consulting_pk>/', views.consulting_detail),
    path('<int:consulting_pk>/answer/', views.answer_create),
]
