# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-05-06 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0012_auto_20190506_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='hotel',
            field=models.CharField(max_length=600, null=True, verbose_name='入住酒店'),
        ),
        migrations.AlterField(
            model_name='journey',
            name='visit_address',
            field=models.CharField(max_length=300, verbose_name='游访地点'),
        ),
    ]
