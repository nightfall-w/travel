# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-05-05 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_auto_20190505_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='hotel',
            field=models.CharField(max_length=100, null=True, verbose_name='入住酒店'),
        ),
    ]
