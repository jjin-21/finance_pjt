from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from finances.models import DepositProducts, SavingProducts

# Create your models here.
class User(AbstractUser):
    # username = models.CharField(max_length=30, unique=True)
    # email = models.EmailField(max_length=50, unique=True)
    # phone_num = PhoneNumberField(unique=True)
    nickname = models.CharField(max_length=20)
    age = models.IntegerField(default=20)
    gender = models.IntegerField(default=1)
    asset = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    deposit = models.ManyToManyField(DepositProducts, blank=True, null=True, related_name="joined_deposit")
    saving = models.ManyToManyField(SavingProducts, blank=True, null=True,related_name="joined_saving")
    created_at = models.DateTimeField(auto_now_add=True)