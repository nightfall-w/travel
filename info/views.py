# -*- coding:utf-8 -*-
import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from info.models import Scheme, Review
from info.serializer import schemeSerializer
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.db.models import Count


class Index(APIView):
    def get(self, request):
        # 获取所有目的地 并去重
        end_locales = set(Scheme.objects.all().values_list('end_locale', flat=True))

        # 获取今年和明年年份
        years = [datetime.datetime.now().year, datetime.datetime.now().year + 1]

        # 获取当天当天日期和一周前一月前日期
        today = datetime.date.today()
        to_date = today + datetime.timedelta(days=1)
        week_ago = today - datetime.timedelta(days=7)
        month_age = today - datetime.timedelta(days=30)
        # 获取最近7天的热点评论(评论数越高,代表热度越高)
        week_hot_review = Review.objects.filter(create__range=(week_ago, to_date))
        # 若最近7天没有热评，就查最近30天的数据
        if not week_hot_review:
            week_hot_review = Review.objects.filter(create__range=(month_age, to_date))
        ss = week_hot_review.only('scheme').values('scheme').annotate(scheme_count=Count("scheme")).order_by(
            '-scheme_count')
        print(ss)
        # schemeSerializer()
        return render(request, 'index.html')


class Result_list(APIView):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, 'result-list.html')


class Result_grid(APIView):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, 'result-grid.html')


class Detail(APIView):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, 'detail-page.html')
