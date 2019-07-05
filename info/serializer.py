# -*- coding:utf-8 -*-
import datetime

from rest_framework import serializers
from django.db.models import Avg


class schemeSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True, max_length=20)
    day = serializers.IntegerField(read_only=True)
    night = serializers.IntegerField(read_only=True)
    favorites = serializers.SerializerMethodField(read_only=True)
    score_avg = serializers.SerializerMethodField(read_only=True, default=4.0)
    photo_url = serializers.SerializerMethodField(read_only=True)
    review_num = serializers.SerializerMethodField(read_only=True)
    unit_price = serializers.SerializerMethodField(read_only=True)

    def get_favorites(self, obj):
        user = self.context['request'].user
        like_schemes = user.scheme_set.all() if user and user.username else []
        favorites = 1 if obj in like_schemes else 0
        return favorites

    def get_score_avg(self, obj):
        score_avg = obj.score.aggregate(Avg('score_number'))['score_number__avg']
        if score_avg is None:
            score_avg = 4
        return score_avg

    def get_photo_url(self, obj):
        journeys = obj.journey_scheme.prefetch_related('scenic').only('scenic')
        if journeys:
            for journey in journeys:
                if not journey.scenic:
                    break
                for scenic in journey.scenic.all():
                    image = scenic.image
                    if image:
                        photo_url = image.url
                        break
                    else:
                        continue
                else:
                    continue
                break
        else:
            photo_url = ''
        return photo_url

    def get_review_num(self, obj):
        review_num = obj.review_scheme.count()
        return review_num

    def get_unit_price(self, obj):
        current_date = datetime.date.today()
        tickets = obj.ticket_scheme.filter(start_date=current_date)
        unit_price = tickets[0].unit_price if tickets else 0
        return unit_price
