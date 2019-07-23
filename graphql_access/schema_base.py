# -*- coding:utf-8 -*-
import graphene
from graphene_mongo.types import MongoengineObjectType

from info.models import Scheme, Ticket, Scenic, Score, Review, Journey


class SubjoinFields(graphene.AbstractType):
    be_like = graphene.Boolean()
    photo_url = graphene.String()


class SchemeType(MongoengineObjectType, SubjoinFields):
    class Meta:
        model = Scheme


class TicketType(MongoengineObjectType):
    class Meta:
        model = Ticket


class ScenicType(MongoengineObjectType):
    class Meta:
        model = Scenic


class ScoreType(MongoengineObjectType):
    class Meta:
        model = Score


class ReviewType(MongoengineObjectType):
    class Meta:
        model = Review


class JourneyType(MongoengineObjectType):
    class Meta:
        model = Journey
