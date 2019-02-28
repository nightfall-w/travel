# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180907_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auth_profile',
            name='phone_number',
            field=models.CharField(verbose_name='???', max_length=11),
        ),
    ]
