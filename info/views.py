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

        # 为找到scheme 返回404页面
        if not scheme:
            return render(request, '404.html')

        # 统计游览景点个数
        scenic_number = 0
        for journey in scheme.journeys:
            scenic_number += len(journey.visit_address)
        scheme.scenic_number = scenic_number

        # 返回3个相似陶套餐(目的地相同)
        similar_schemes = Scheme.objects.filter(Q(destination=scheme.destination) & Q(_id__ne=scheme._id))[0:3]

        # 返回评分信息
        if 4.5 <= scheme.avg_score <= 5:
            level = "极好"
        elif 4 <= scheme.avg_score < 4.5:
            level = "优秀"
        elif 3 <= scheme.avg_score < 4:
            level = "良好"
        else:
            level = "一般"


        """
            Mock 数据
        """
        # 评分排名
        all_scheme_score = [scheme.avg_score for scheme in Scheme.objects.all()]
        all_scheme_score.sort()
        all_scheme_score = all_scheme_score[::-1]
        all_scheme_len = len(all_scheme_score)
        index = all_scheme_score.index(scheme.avg_score, -1)
        score_ranking = "%.2f%%" % (index / all_scheme_len * 100)

        # 清洁分
        cleanliness = 3.4
        cleanliness_score_count = 133
        cleanliness_percentage = "%.2f" % (cleanliness / 5 * 100)
        # 服务
        service = 4.6
        service_score_count = 133
        service_percentage = "%.2f" % (service / 5 * 100)
        # 舒适
        comfortable = 4.2
        comfortable_score_count = 133
        comfortable_percentage = "%.2f" % (comfortable / 5 * 100)
        # 条件
        condition = 4.7
        condition_score_count = 133
        condition_percentage = "%.2f" % (condition / 5 * 100)

        return render(request, 'detail-page.html',
                      {'scheme': scheme, 'similar_schemes': similar_schemes, 'avg_score': scheme.avg_score,
                       'level': level, 'score_ranking': score_ranking, 'cleanliness': cleanliness,
                       'cleanliness_percentage': cleanliness_percentage, 'service': service,
                       'service_percentage': service_percentage, 'comfortable': comfortable,
                       'comfortable_percentage': comfortable_percentage, 'condition': condition,
                       'condition_percentage': condition_percentage, 'cleanliness_score_count': cleanliness_score_count,
                       'service_score_count': service_score_count, 'comfortable_score_count': comfortable_score_count,
                       'condition_score_count': condition_score_count})


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
    推荐受关注的目的地
    '''

    def get(self, request):
        # 推荐一些受关注目的地的scheme
        schemes = Scheme.objects.order_by('-avg_score')[0:4]
        schemes_json = spotSchemeSerializer(schemes, many=True)
        return Response(schemes_json.data)
