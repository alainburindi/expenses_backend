import graphene

from .mutations.create_user import CreateUser


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
