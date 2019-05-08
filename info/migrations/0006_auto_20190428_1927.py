# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-04-28 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_auto_20190427_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journey',
            name='cafe',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='hotel',
        ),
        migrations.AddField(
            model_name='journey',
            name='hotel',
            field=models.CharField(default='', max_length=100, verbose_name='入住酒店'),
        ),
        migrations.AddField(
            model_name='scheme',
            name='feature',
            field=models.TextField(default='', verbose_name='特色'),
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
    ]
