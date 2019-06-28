# -*- coding:utf-8 -*-
import graphene
from graphene_django.types import DjangoObjectType

from info.models import Scheme, Ticket, Scenic, Score, Review, Journey


class UserFields(graphene.AbstractType):
    price = graphene.Int()
    grade = graphene.Float()
    be_like = graphene.Boolean()
    review_num = graphene.Int()
    photo_url = graphene.String()


class SchemeType(DjangoObjectType, UserFields):
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
