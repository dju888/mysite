from django.db import models

# Create your models here.
class zhuan_jia_lie_biao(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    tou_xiang = models.CharField(max_length=200)
    zhuan_ye = models.CharField(max_length=200)
    emial = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    bi_ye_xue_yuan = models.CharField(max_length=200)
    xue_wei = models.CharField(max_length=200)
    dan_wei = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    ge_ren_jian_jie = models.CharField(max_length=200)
    hang_ye_lei_bie = models.CharField(max_length=200)