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
        fields = ['_id', 'title', 'day', 'night', 'review', 'scenic_images', 'avg_score', 'price']


class spotSchemeSerializer(serializers.DocumentSerializer):
    '''
    热门套餐的序列化器
    '''

    class Meta:
        model = Scheme
        fields = ['_id', 'destination', 'price', 'scenic_images']


# class detaliSchemeSerializer(serializers.DocumentSerializer):
#     '''
#     套餐详情的序列化器
#     '''
#
#     class Meta:
#         model = Scheme
#         fields = '__all__'
