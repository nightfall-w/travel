# -*- coding:utf-8 -*-
import datetime

from info.models import Scheme
from rest_framework_mongoengine import serializers


class schemeSerializer(serializers.DocumentSerializer):
    '''
    schemes序列化器(DocumentSerializer继承自drf中的ModelSerializer，用于代替ModelSerializer序列化mongodb中的document)
    '''

    class Meta:
        model = Scheme
        fields = ['name', 'day', 'night', 'review_number', 'first_photo', 'avg_score', 'min_price']


class spotSchemeSerializer(serializers.DocumentSerializer):
    '''
    热门套餐的序列化器
    '''

    class Meta:
        model = Scheme
        fields = ['end_locale', 'min_price', 'first_photo']
