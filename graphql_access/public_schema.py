# -*- coding:utf-8 -*-
from rest_framework.pagination import LimitOffsetPagination, _positive_int
from rest_framework.views import APIView

from graphql_access.schema_base import *


class MyLimitOffsetPagination(LimitOffsetPagination):
    # 默认显示的个数
    default_limit = 12
    # 当前的位置
    offset_query_param = "offset"
    # 通过limit改变默认显示的个数
    limit_query_param = "limit"
    # 一页最多显示的个数
    max_limit = 18

    def get_limit(self, request):
        # 重写了MyLimitOffsetPagination获取limit的方法，之前的get_limit是从request的GET中取
        try:
            if self.limit_query_param:
                return _positive_int(
                    request.limit,
                    strict=True,
                    cutoff=self.max_limit
                )
            return self.default_limit
        except:
            return self.default_limit

    def get_offset(self, request):
        # 同get_offset,只是取offset
        try:
            return _positive_int(
                request.offset,
            )
        except:
            return 0


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
    scheme = graphene.List(SchemeType, limit=graphene.Int(), offset=graphene.Int())
    ticket = graphene.List(TicketType)

    def resolve_scheme(self, info, **kwargs):
        # 返回套餐数据
        schemes = Scheme.objects.all()
        pg = MyLimitOffsetPagination()
        request = APIView().initialize_request(info.context)
        if kwargs.get('limit'):
            request.limit = kwargs.get('limit')
        if kwargs.get('offset'):
            request.offset = kwargs.get('offset')
        page_schemes = pg.paginate_queryset(queryset=schemes, request=request)
        return page_schemes

    def resolve_ticket(self, info, **kwargs):
        # 返回指定scheme
        tickets = Ticket.objects.all()
        return tickets
