# -*- coding:utf-8 -*-
import datetime
import random
from django.shortcuts import render
from rest_framework.views import APIView
from info.models import Scheme, Review, Ticket
from info.serializer import schemeSerializer, scenicSpotSerializer
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.db.models import Count, Avg, Min, Max


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
        week_hot_review = Review.objects.filter(create__range=(week_ago, to_date))
        if not week_hot_review:
            week_hot_review = Review.objects.filter(create__range=(month_age, to_date))
        sort_schemes = week_hot_review.only('scheme').values('scheme').annotate(scheme_count=Count("scheme")).order_by(
            '-scheme_count')
        most_hot_schemes = sort_schemes[0:9]
        schemeIdList = [schemeInfo['scheme'] for schemeInfo in most_hot_schemes]
        hot_schemes = Scheme.objects.prefetch_related('score').filter(id__in=schemeIdList)
        schemes_json = schemeSerializer(hot_schemes, context={"request": request}, many=True)
        return Response(schemes_json.data)


class Scenic_spot(APIView):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        # 随机推荐一些scheme
        today = datetime.date.today()
        tickets = Ticket.objects.filter(start_date=today).select_related('scheme')
        recommended_schemes = []
        for _ in range(4):
            ticket = random.choice(tickets)
            if ticket.scheme not in recommended_schemes:
                recommended_schemes.append(ticket.scheme)

        recommended_schemes_json = scenicSpotSerializer(recommended_schemes, many=True)
        # end_locales = Scheme.objects.all().values('end_locale').annotate(end_locale_num=Count('end_locale')).order_by(
        #     '-end_locale_num')
        # for end_locale in end_locales[0:4]:
        #     schemes = Scheme.objects.filter(end_locale=end_locale['end_locale'])
        #     min_price_scheme = {}
        #     for scheme in schemes:
        #         ticket = scheme.ticket_scheme.filter(start_date=today)
        #         if ticket:
        #             min_price_scheme[scheme] = ticket[0].unit_price



        return Response(recommended_schemes_json.data)
