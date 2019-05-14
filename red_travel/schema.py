# -*- coding: utf-8 -*-
# 总的schema入口

import graphene
from graphql_access import public_schema, private_schema


class PublicQuery(public_schema.Query, graphene.ObjectType):
    # 总的Public Schema的query入口
    pass


class PublicMutations(graphene.ObjectType):
    # 总的Public Schema的mutations入口
    UserFavorites = public_schema.UserFavorites.Field()


PublicSchema = graphene.Schema(query=PublicQuery, mutation=PublicMutations)


class PrivateQuery(private_schema.Query, graphene.ObjectType):
    # 总的Private Schema的query入口
    pass


class PrivateMutations(graphene.ObjectType):
    # 总的Private Schema的mutations入口
    UserFavorites = private_schema.UserFavorites.Field()


PrivateSchema = graphene.Schema(query=PrivateQuery, mutation=PrivateMutations)
