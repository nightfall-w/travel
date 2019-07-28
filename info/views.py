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
    def get(self, request, *args, **kwargs):
        destination = request.GET.getlist('destination', None)
        month = request.GET.getlist('month')
        year = request.GET.getlist('year', None)
        end_locales = Scheme.objects.distinct('end_locale')
        years = [str(datetime.datetime.now().year), str(datetime.datetime.now().year + 1)]
        result = {'select_destination': destination, 'select_months': month, 'select_years': year,
                  'end_locales': end_locales, 'years': years, 'months': [str(i) for i in range(13)]}
        return render(request, 'result-list.html', result)


class Result_grid(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'result-grid.html')


class Detail(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'detail-page.html')


class Schemes(APIView):
    '''
    推荐热门的套餐
    '''

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
    '''
    推荐热门目的地
    '''

    def get(self, request):
        # 推荐一些受关注目的地的scheme
        schemes = Scheme.objects.order_by('-favorites')[0:4]
        schemes_json = spotSchemeSerializer(schemes, many=True)
        return Response(schemes_json.data)

# class IndexSearch(APIView):
#     '''
#         根据首页搜索条件返回result模板
#     '''
#     def get(self, request):
