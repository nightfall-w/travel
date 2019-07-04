import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from info.models import Scheme, Review
from info.serializer import schemeSerializer
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.db.models import Count

# Create your views here.

class Index(APIView):
    def get(self, request):
        # ???????? ???
        end_locales = set(Scheme.objects.all().values_list('end_locale', flat=True))

        # ???????????????
        years = [datetime.datetime.now().year, datetime.datetime.now().year + 1]

        # ????????????????????
        today = datetime.date.today()
        to_date = today + datetime.timedelta(days=1)
        week_ago = today - datetime.timedelta(days=7)
        month_age = today - datetime.timedelta(days=30)
        # ????????(????? ?????)
        week_hot_review = Review.objects.filter(create__range=(week_ago, to_date))
        if not week_hot_review:
            week_hot_review = Review.objects.filter(create__range=(week_ago, to_date))
        ss = week_hot_review.only('scheme').order_by("scheme")
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
