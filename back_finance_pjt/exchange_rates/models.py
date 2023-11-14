from django.db import models

# Create your models here.
class ExchangeRate(models.Model):
    cur_nm = models.TextField()
    cur_unit = models.TextField()
    ttb = models.TextField()
    tts = models.TextField()
    deal_bas_r = models.TextField()
    result = models.IntegerField()