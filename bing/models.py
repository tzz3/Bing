from django.db import models


class Images(models.Model):
    startdate = models.CharField(max_length=8)
    fullstartdate = models.CharField(max_length=12)
    enddate = models.CharField(max_length=8)
    # URLField 用于保存URL
    url = models.CharField(max_length=200)
    urlbase = models.CharField(max_length=200)
    copyright = models.CharField(max_length=200)
    copyrightlink = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    quiz = models.CharField(max_length=200)
    wp = models.BooleanField
    hsh = models.CharField(max_length=200)
    drk = models.CharField(max_length=200)
    top = models.CharField(max_length=200)
    bot = models.CharField(max_length=200)
    hs = models.CharField(max_length=200)

    path = models.CharField(max_length=200)  # 图片服务器存储路径
