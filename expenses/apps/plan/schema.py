import graphene

from .mutations.create import CreatePlan


class Mutation(graphene.ObjectType):
    create_plan = CreatePlan.Field()
