from django.db import models


class Images(models.Model):
    startdate = models.CharField(max_length=8, null=True)
    fullstartdate = models.CharField(max_length=12, null=True)
    enddate = models.CharField(max_length=8, null=True)
    # URLField 用于保存URL
    url = models.CharField(max_length=200, null=True)
    urlbase = models.CharField(max_length=200, null=True)
    copyright = models.CharField(max_length=200, null=True)
    copyrightlink = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    quiz = models.CharField(max_length=200, null=True)
    wp = models.BooleanField  # fixme 无法在管理界面输入
    hsh = models.CharField(max_length=200, null=True)
    drk = models.CharField(max_length=200, null=True)
    top = models.CharField(max_length=200, null=True)
    bot = models.CharField(max_length=200, null=True)
    hs = models.CharField(max_length=200, null=True)

    path = models.CharField(max_length=200, null=True)  # 图片服务器存储路径

    def __str__(self):
        return self.path
