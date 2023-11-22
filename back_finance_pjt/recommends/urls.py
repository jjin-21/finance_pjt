from django.urls import path
from . import views

app_name = "recommends"
urlpatterns = [
    path('<int:user_pk>/', views.recommend)
]
