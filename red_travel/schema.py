# -*- coding: utf-8 -*-
# 总的schema入口

import graphene
import info.schema


class PublicQuery(info.schema.Query, graphene.ObjectType):
    # 总的Public Schema的query入口
    pass


class PublicMutations(graphene.ObjectType):
    # 总的Public Schema的mutations入口
    UserFavorites = info.schema.UserFavorites.Field()


public_schema = graphene.Schema(query=PublicQuery, mutation=PublicMutations)


class PrivateQuery(info.schema.Query, graphene.ObjectType):
    # 总的Private Schema的query入口
    pass


class PrivateMutations(graphene.ObjectType):
    # 总的Private Schema的mutations入口
    UserFavorites = info.schema.UserFavorites.Field()


private_schema = graphene.Schema(query=PrivateQuery, mutation=PrivateMutations)
