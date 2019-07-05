# -*- coding:utf-8 -*-
import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from info.models import Scheme, Review
from info.serializer import schemeSerializer
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.db.models import Count, Avg


class Index(APIView):
    def get(self, request):
        end_locales = set(Scheme.objects.all().values_list('end_locale', flat=True))
        years = [datetime.datetime.now().year, datetime.datetime.now().year + 1]
        return render(request, 'index.html', {'end_locales': end_locales, 'years': years})


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


class Schemes(APIView):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        today = datetime.date.today()
        to_date = today + datetime.timedelta(days=1)
        week_ago = today - datetime.timedelta(days=7)
        month_age = today - datetime.timedelta(days=30)
        # èŽ·å�–æœ€è¿‘7å¤©çš„çƒ­ç‚¹è¯„è®º(è¯„è®ºæ•°è¶Šé«˜,ä»£è¡¨çƒ­åº¦è¶Šé«˜)
        week_hot_review = Review.objects.filter(create__range=(week_ago, to_date))
        # è‹¥æœ€è¿‘7å¤©æ²¡æœ‰çƒ­è¯„ï¼Œå°±æŸ¥æœ€è¿‘30å¤©çš„æ•°æ�®
        if not week_hot_review:
            week_hot_review = Review.objects.filter(create__range=(month_age, to_date))
        sort_schemes = week_hot_review.only('scheme').values('scheme').annotate(scheme_count=Count("scheme")).order_by(
            '-scheme_count')
        most_hot_schemes = sort_schemes[0:10]
        schemeIdList = [schemeInfo['scheme'] for schemeInfo in most_hot_schemes]
        hot_schemes = Scheme.objects.prefetch_related('score').filter(id__in=schemeIdList)
        schemes_json = schemeSerializer(hot_schemes, context={"request": request}, many=True)
        return Response(schemes_json.data)
