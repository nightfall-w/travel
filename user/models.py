# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Auth_profile(models.Model):
    phone_number = models.CharField(max_length=11, verbose_name='手机号')
    user_obj = models.OneToOneField(User, on_delete=models.CASCADE)
    head_photo = models.FilePathField(
        path='media/head_portrait',
        default='/media/head_portrait/default.jepg')

    class Meta:
        db_table = 'auth_profile'
        verbose_name = verbose_name_plural = '用户信息'

    def __str__(self):
        return self.phone_number
