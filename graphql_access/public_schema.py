# -*- coding:utf-8 -*-
import graphene

from graphql_access.schema_base import *

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

    def resolve_all_scheme(self, info, **kwargs):
        schemes = Scheme.objects.all()
        return schemes

    def resolve_all_ticket(self, info, **kwargs):
        tickets = Ticket.objects.all()
        return tickets
