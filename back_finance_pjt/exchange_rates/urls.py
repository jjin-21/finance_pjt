from django.urls import path
from . import views

app_name = 'exchange-rates'
urlpatterns = [
    path('calculator/',views.calculator, name='calculator'),
    path('save/',views.save, name='save'),
]
