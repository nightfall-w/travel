# -*- coding:utf-8 -*-
import datetime
import random

from django.shortcuts import render
from mongoengine.queryset.visitor import Q
from rest_framework.response import Response
from rest_framework.views import APIView

from info.models import Scheme
from info.serializer import schemeSerializer, spotSchemeSerializer


class Index(APIView):
    def get(self, request):
        end_locales = Scheme.objects.distinct('destination')
        years = [datetime.datetime.now().year, datetime.datetime.now().year + 1]
        return render(request, 'index.html', {'end_locales': end_locales, 'years': years})


class ResultList(APIView):
    def get(self, request, *args, **kwargs):
        destination_select = request.GET.getlist('destination', None)
        month = request.GET.getlist('month', None)
        year = request.GET.getlist('year', None)
        destination_all = Scheme.objects.distinct('destination')
        months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        years = [str(datetime.datetime.now().year), str(datetime.datetime.now().year + 1)]
        result = {'destination_select': destination_select, 'select_months': month, 'select_years': year,
                  'destinations': destination_all, 'years': years, 'months': months}
        return render(request, 'result-list.html', result)


class ResultGrid(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'result-grid.html')


class Detail(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        scheme = Scheme.objects.filter(_id=id).first()
        if not scheme:
            return render(request, '404.html')
        scenic_number = 0
        for journey in scheme.journeys:
            for scenic in journey.visit_address:
                scenic_number += 1
        scheme.scenic_number = scenic_number

        similar_schemes = Scheme.objects.filter(Q(destination=scheme.destination) & Q(_id__ne=scheme._id))[0:3]

        return render(request, 'detail-page.html', {'scheme': scheme, 'similar_schemes': similar_schemes})


class Schemes(APIView):
    '''
    推荐热门的套餐
    '''

    def get(self, request):
        schemes = Scheme.objects.all()
        hot_schemes = dict()
        sign = 9
        while sign > 0:
            scheme = random.choice(schemes)
            if scheme._id not in hot_schemes.keys():
                hot_schemes[scheme._id] = scheme
                sign -= 1
            else:
                continue
        schemes_json = schemeSerializer(hot_schemes.values(), many=True)
        return Response(schemes_json.data)


class ScenicSpot(APIView):
    '''
    推荐热门目的地
    '''

    def get(self, request):
        # 推荐一些受关注目的地的scheme
        schemes = Scheme.objects.order_by('-avg_score')[0:4]
        schemes_json = spotSchemeSerializer(schemes, many=True)
        return Response(schemes_json.data)
