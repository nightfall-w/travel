# -*- coding:utf-8 -*-
from graphene_django.types import DjangoObjectType

from info.models import Scheme, Ticket, Scenic, Score, Review, Journey


class SchemeType(DjangoObjectType):
    class Meta:
        model = Scheme


class TicketType(DjangoObjectType):
    class Meta:
        model = Ticket


class ScenicType(DjangoObjectType):
    class Meta:
        model = Scenic


class ScoreType(DjangoObjectType):
    class Meta:
        model = Score


class ReviewType(DjangoObjectType):
    class Meta:
        model = Review


class JourneyType(DjangoObjectType):
    class Meta:
        model = Journey
