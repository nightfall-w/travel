# -*- coding:utf-8 -*-
import datetime
import graphene
from rest_framework.pagination import LimitOffsetPagination, _positive_int
from rest_framework.views import APIView

from graphql_access.schema_base import *
from graphql_access.utils import SORTKEY


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
        # 与get_offset同理,只是取offset
        try:
            return _positive_int(
                request.offset,
            )
        except:
            return 0


class PageSchemeType(graphene.ObjectType):
    total = graphene.Int()
    limit = graphene.Int()
    offset = graphene.Int()
    sort_by = graphene.Int()
    page_scheme = graphene.List(SchemeType)

    def resolve_page_scheme(self, info):
        '''
        根据过滤条件 返回对应的schemes数据
        :param info:
        :return: 过滤并分页后的schemes queryset
        '''
        # 看sort条件是否在规定符合规定，0表示默认，不排序）
        self.sort_by = self.sort_by if self.sort_by in SORTKEY.keys() else 0
        sort_key = SORTKEY[self.sort_by]
        if abs(self.sort_by) == 1:
            # 根据scheme name进行排序
            schemes = Scheme.objects.order_by(sort_key)
        elif abs(self.sort_by) == 2:
            # 根据当日价格排序
            current_date = datetime.date.today()
            # scheme_id_tuple = tuple(
            #     Ticket.objects.filter(start_date=current_date).order_by(sort_key).values_list('scheme',
            #                                                                                   flat=True))
            schemes = [ticket.scheme for ticket in
                       Ticket.objects.order_by(sort_key).select_related('scheme').filter(start_date=current_date).only('scheme')]
            # schemes = list()
            # for scheme_id in scheme_id_tuple:
            #     scheme_obj = Scheme.objects.get(id=scheme_id)
            #     schemes.append(scheme_obj)
        elif abs(self.sort_by) == 3:
            # 根据目的地排序
            schemes = Scheme.objects.order_by(self.sort_by)
        elif abs(self.sort_by) == 4:
            schemes = Scheme.objects.all().prefetch_related('score')
            for scheme in schemes:
                print(scheme.score)
            print(schemes)
        else:
            schemes = Scheme.objects.all()
        pg = MyLimitOffsetPagination()
        request = APIView().initialize_request(info.context)
        if self.limit:
            request.limit = self.limit
        if self.offset:
            request.offset = self.offset
        page_schemes = pg.paginate_queryset(queryset=schemes, request=request)
        return page_schemes


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
    page_schemes = graphene.List(PageSchemeType, limit=graphene.Int(), offset=graphene.Int(), sort_by=graphene.Int())
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
        for scheme in page_schemes:
            scheme.total = len(schemes)
        return page_schemes

    def resolve_page_schemes(self, info, **kwargs):
        # 返回套餐数据
        total_schemes = len(Scheme.objects.all())
        return [PageSchemeType(limit=kwargs.get('limit', None), offset=kwargs.get('offset', None),
                               sort_by=kwargs.get('sort_by', 0))]

    def resolve_ticket(self, info, **kwargs):
        # 返回指定scheme
        tickets = Ticket.objects.all()
        return tickets
