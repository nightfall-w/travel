# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-06-28 14:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0015_auto_20190625_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='scheme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journey_scheme', to='info.Scheme', verbose_name='所属套餐'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='scheme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticker_scheme', to='info.Scheme', verbose_name='套餐对象'),
        ),
    ]