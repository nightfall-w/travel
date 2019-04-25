# -*- coding:utf-8 -*-
import graphene
from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import User
from info.models import Scheme, Ticket, Scenic, Score, Review, Journey, Groggery


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


class GroggeryType(DjangoObjectType):
    class Meta:
        model = Groggery


class SchemeListType(DjangoObjectType):
    class Meta:
        model = Scheme
    is_favorites = graphene.Boolean()
    review_number = graphene.Int()
    score_result = graphene.Int()



# 定义Mutation元素输入类型
class SchemeInput(graphene.InputObjectType):
    scheme_id = graphene.Int(required=True)


# 定义一个用户喜欢某个scheme的mutation
class UserFavorites(graphene.Mutation):
    # api的输入参数
    class Arguments:
        scheme_data = SchemeInput(required=True)

    # api的响应参数
    ok = graphene.Boolean()

    # api的相应操作  绑定当前用户喜欢指定套餐
    def mutate(self, info, scheme_data):
        user = info.context.user
        if user.id:
            try:
                Scheme.objects.get(id=scheme_data['scheme_id']).favorites.add(user)
                ok = True
            except Scheme.DoesNotExist:
                ok = False
        else:
            ok = False
        return UserFavorites(ok=ok)


class Query(object):
    all_scheme = graphene.List(SchemeType)
    all_ticket = graphene.List(TicketType)

    scheme_list = graphene.List(SchemeListType, originating=graphene.String(), end_locale=graphene.String(),
                                year=graphene.Int(),
                                month=graphene.Int(), scheme_name=graphene.String(), min_price=graphene.Int(),
                                max_price=graphene.Int(),
                                score=graphene.Int())

    def resolve_all_scheme(self, info, **kwargs):
        schemes = Scheme.objects.all()
        return schemes

    def resolve_all_ticket(self, info, **kwargs):
        tickets = Ticket.objects.all()
        return tickets

    def resolve_scheme_list(self, info, **kwargs):
        originating = kwargs.get('originating', None)
        end_locale = kwargs.get('end_locale', None)
        year = kwargs.get('end_locale', None)
        month = kwargs.get('month', None)
        scheme_name = kwargs.get('scheme_name', None)
        min_price = kwargs.get('min_price', None)
        max_price = kwargs.get('max_price', None)
        score = kwargs.get('score', None)
        schemes = Scheme.objects.all()
        for i in schemes:
            i.is_favorites = True
            i.review_number = 6
            i.score_result = 6
        return schemes
