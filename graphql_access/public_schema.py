# -*- coding:utf-8 -*-
import datetime

from rest_framework.pagination import LimitOffsetPagination, _positive_int
from rest_framework.views import APIView

from graphql_access.schema_base import *
from graphql_access.utils import SORTKEY
from info.models import User


class PageSchemeType(graphene.ObjectType):
    total = graphene.Int()
    limit = graphene.Int()
    offset = graphene.Int()
    sort_by = graphene.Int()
    year_month = graphene.List(graphene.String)
    destinations = graphene.List(graphene.String)
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
        if not self.limit:
            self.limit = -1
        if self.offset:
            self.offset = 0
        # 0 根据id进行排序
        # 1 根据价格排序
        # 2 根据评分进行排序
        if self.limit == -1:
            page_schemes = Scheme.objects.filter(destination__in=self.destinations,
                                                 ticket_month__in=self.year_month).order_by(sort_key)[
                           self.offset::]
        else:
            page_schemes = Scheme.objects.filter(destination__in=self.destinations,
                                                 ticket_month__in=self.year_month).order_by(sort_key)[
                           self.offset:self.limit + self.offset]
        # 获取当前登录用户
        uid = info.context.user.id
        if uid:
            user = User.objects.filter(uid=uid).first()
        else:
            user = None
        # 为分页后的套餐实现抽象的属性
        for scheme in page_schemes:
            # 如果user存在于scheme中,那be_like为1,表示用户喜欢这个此套餐,否则反之
            scheme.be_like = 1 if user and user in scheme.favorites else 0
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
    page_schemes = graphene.List(PageSchemeType, limit=graphene.Int(), offset=graphene.Int(), sort_by=graphene.Int(),
                                 destinations=graphene.String(), months=graphene.String(), years=graphene.String())

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

    def resolve_page_schemes(self, info, **kwargs):
        limit = kwargs.get('limit', None)
        offset = kwargs.get('offset', None)
        sort_key = kwargs.get('sort_by', 0)
        destinations = kwargs.get('destinations', None)
        if destinations:
            destinations = eval(destinations)
        else:
            destinations = Scheme.objects.distinct('destination')
        year_month = []
        months = kwargs.get('months', None)
        if months:
            months = eval(months)
        else:
            months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        years = kwargs.get('years', None)
        if years:
            years = eval(years)
        else:
            years = [str(datetime.datetime.now().year), str(datetime.datetime.now().year + 1)]
        for year in years:
            for month in months:
                year_month.append(year + '-' + month)
        sort_key = sort_key if sort_key in SORTKEY.keys() else 0
        total_schemes = Scheme.objects.filter(destination__in=destinations, ticket_month__in=year_month).count()
        return [PageSchemeType(limit=limit, offset=offset, sort_by=sort_key, total=total_schemes, year_month=year_month,
                               destinations=destinations)]
