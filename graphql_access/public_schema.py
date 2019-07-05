# -*- coding:utf-8 -*-
import datetime

from rest_framework.pagination import LimitOffsetPagination, _positive_int
from rest_framework.views import APIView

from django.db.models import Avg

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
        current_date = datetime.date.today()
        if abs(self.sort_by) == 1:
            # 根据scheme name进行排序
            schemes = Scheme.objects.order_by(sort_key)
        elif abs(self.sort_by) == 2:
            # 根据当日价格排序
            schemes = [ticket.scheme for ticket in
                       Ticket.objects.order_by(sort_key).select_related('scheme').filter(start_date=current_date).only(
                           'scheme')]
        elif abs(self.sort_by) == 3:
            # 根据目的地排序
            schemes = Scheme.objects.order_by(sort_key)
        elif abs(self.sort_by) == 4:
            # 根据评分进行排序
            schemes = Scheme.objects.prefetch_related('score')
            schemes_dict = dict()
            for scheme in schemes:
                # 遍历scheme对象，拿到对应的平均评分，结果形式为  例:{'score_number__avg':4.6}
                score_avg = scheme.score.aggregate(Avg('score_number'))
                # 如果scheme(套餐还未被评分，为None，我们设为4)
                if score_avg['score_number__avg'] is None:
                    score_avg['score_number__avg'] = 4
                schemes_dict[scheme] = score_avg['score_number__avg']
            if self.sort_by == 4:
                # 将schemes由评由高到低排序，默认
                schemes = sorted(schemes_dict, key=schemes_dict.__getitem__, reverse=True)
            else:
                # 将schemes由评分由低到高排序
                schemes = sorted(schemes_dict, key=schemes_dict.__getitem__)
        else:
            schemes = Scheme.objects.all()

        # 实例化我们的分页类
        pg = MyLimitOffsetPagination()
        # 将graphql封装为restful 的request    封装前request = info.context
        request = APIView().initialize_request(info.context)
        if self.limit:
            request.limit = self.limit
        if self.offset:
            request.offset = self.offset
        page_schemes = pg.paginate_queryset(queryset=schemes, request=request)

        # 获取当前登录用户所喜欢的所有套餐
        user = request.user
        like_schemes = user.scheme_set.all() if user and user.username else []
        # 为分页后的套餐实现抽象的属性
        for scheme in page_schemes:
            journeys = scheme.journey_scheme.prefetch_related('scenic').only('scenic')
            if journeys:
                for journey in journeys:
                    if not journey.scenic:
                        break
                    for scenic in journey.scenic.all():
                        image = scenic.image
                        if image:
                            scheme.photo_url = image.url
                            break
                        else:
                            continue
                    else:
                        continue
                    break
            else:
                scheme.photo_url = ''
            tickets = scheme.ticket_scheme.filter(start_date=current_date)
            score_avg = scheme.score.aggregate(Avg('score_number'))
            review_num = scheme.review_scheme.count()
            scheme.grade = '%.1' % score_avg['score_number__avg'] if score_avg['score_number__avg'] else 4.0
            scheme.price = tickets[0].unit_price if tickets else 0
            scheme.be_like = 1 if scheme in like_schemes else 0
            scheme.review_num = review_num
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
        limit = kwargs.get('limit', None)
        offset = kwargs.get('offset', None)
        sort_key = kwargs.get('sort_by', 0)
        sort_key = sort_key if sort_key in SORTKEY.keys() else 0
        sort_by = SORTKEY[sort_key]
        if abs(sort_key) == 2:
            # 因为要根据当天票的价格排序 所以只查找当天有票的套餐
            current_date = datetime.date.today()
            schemes = Ticket.objects.order_by(sort_by).select_related('scheme').filter(start_date=current_date).only(
                'scheme')
        else:
            # 否则其他排序方式都是查所有的套餐
            schemes = Scheme.objects.all()
        total_schemes = len(schemes)
        return [PageSchemeType(limit=limit, offset=offset, sort_by=sort_key, total=total_schemes)]

    def resolve_ticket(self, info, **kwargs):
        # 返回指定scheme
        tickets = Ticket.objects.all()
        return tickets
