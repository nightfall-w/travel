# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-06-28 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0017_auto_20190628_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='assist',
            field=models.BigIntegerField(blank=True, verbose_name='赞同数'),
        ),
        migrations.AlterField(
            model_name='review',
            name='oppose',
            field=models.BigIntegerField(blank=True, verbose_name='反对数'),
        ),
    ]