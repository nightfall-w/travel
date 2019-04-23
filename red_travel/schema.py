# -*- coding: utf-8 -*-
# 总的schema入口

import graphene
import info.schema

# class Query(info.schema.Query, graphene.ObjectType):
#     # 总的Schema的query入口
#     pass

class Mutations(graphene.ObjectType):
    # 总的Schema的mutations入口
    UserFavorites = info.schema.UserFavorites.Field()

schema = graphene.Schema(mutation=Mutations)