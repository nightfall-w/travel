import graphene

from graphql_access.schema_base import *

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

    def resolve_all_scheme(self, info, **kwargs):
        schemes = Scheme.objects.all()
        return schemes

    def resolve_all_ticket(self, info, **kwargs):
        tickets = Ticket.objects.all()
        return tickets

