# -*- coding:utf-8 -*-
import datetime
import random
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from info.models import Scheme
from info.serializer import schemeSerializer, spotSchemeSerializer


class Index(APIView):
    def get(self, request):
        end_locales = Scheme.objects.distinct('end_locale')
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
        schemes = Scheme.objects.filter(review_number__gt=0)
        hot_schemes = list()
        sign = 9
        while sign > 0:
            scheme = random.choice(schemes)
            if scheme not in hot_schemes:
                hot_schemes.append(scheme)
                sign -= 1
            else:
                continue
        schemes_json = schemeSerializer(hot_schemes, many=True)
        return Response(schemes_json.data)


class Scenic_spot(APIView):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        # 推荐一些受关注目的地的scheme
        schemes = Scheme.objects.order_by('-favorites')[0:4]
        schemes_json = spotSchemeSerializer(schemes, many=True)
        return Response(schemes_json.data)
