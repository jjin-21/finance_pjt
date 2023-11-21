from django.db import models
from django.contrib.auth.models import AbstractUser
from finances.models import DepositProducts, SavingProducts

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=50, unique=True)
    company = models.CharField(max_length=20)
    is_fin_job = models.IntegerField(default=0)
    phone_num = models.CharField(max_length=20, unique=True)
    nickname = models.CharField(max_length=20, unique=True)
    age = models.IntegerField(default=20)
    gender = models.IntegerField(default=1)
    asset = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    deposit = models.ManyToManyField(DepositProducts, blank=True, null=True, related_name="joined_deposit")
    saving = models.ManyToManyField(SavingProducts, blank=True, null=True,related_name="joined_saving")
    created_at = models.DateTimeField(auto_now_add=True)