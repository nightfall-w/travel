# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-07-05 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0020_auto_20190701_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenic',
            name='image',
            field=models.ImageField(upload_to='images/scenic', verbose_name='景点照片'),
        ),
    ]