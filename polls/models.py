import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    # 问题描述
    question_text = models.CharField(max_length=200)
    # 发布时间
    pub_date = models.DateTimeField('data published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 选项描述
    choice_text = models.CharField(max_length=200)
    # 当前得票数
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
