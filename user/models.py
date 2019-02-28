# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class auth_profile(models.Model):
    phone_number = models.CharField(max_length=11, verbose_name='手机号')
    user_obj = models.ForeignKey(User)

    class Meta:
        db_table = 'auth_profile'
