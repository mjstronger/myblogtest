from django.db import models

import django.utils.timezone as timezone


class Article(models.Model):
    title = models.CharField(max_length=32,default='Title')#文章标题最大长度32，默认叫Title
    content = models.TextField(null=True)#文章内容允许为空
    date_add = models.DateTimeField(auto_now=False,auto_now_add=False,default=timezone.now)
    # writer = models.CharField(max_length=32,default='admin')

    def __str__(self):
        return self.title#使文章名字显示在管理界面显示粗来
