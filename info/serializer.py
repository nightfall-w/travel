# -*- coding:utf-8 -*-

from rest_framework import serializers


class schemeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20, required=True)
    day = serializers.IntegerField(required=True)
    night = serializers.IntegerField(required=True)
    beLike = serializers.BooleanField(default=False, required=True)
    scenic = serializers.FloatField(default=4.0, required=True)
    photoUrl = serializers.CharField(max_length=200, required=True)
    reviewNum = serializers.IntegerField(required=True)
    unit_price = serializers.IntegerField(required=True)

