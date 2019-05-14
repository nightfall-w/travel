import graphene

from graphql_access.schema_base import *


class SchemeListType(DjangoObjectType):
    class Meta:
        model = Scheme

    is_favorites = graphene.Boolean()
    review_number = graphene.Int()
    score_result = graphene.Int()


# ??Mutation??????
class SchemeInput(graphene.InputObjectType):
    scheme_id = graphene.Int(required=True)


# ??????????scheme?mutation
class UserFavorites(graphene.Mutation):
    # api?????
    class Arguments:
        scheme_data = SchemeInput(required=True)

    # api?????
    ok = graphene.Boolean()

    # api?????  ????????????
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
