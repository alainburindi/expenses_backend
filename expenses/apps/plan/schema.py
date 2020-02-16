import graphene

from .mutations.create import CreatePlan
from .mutations.update import UpdatePlan


class Mutation(graphene.ObjectType):
    create_plan = CreatePlan.Field()
    update_plan = UpdatePlan.Field()
