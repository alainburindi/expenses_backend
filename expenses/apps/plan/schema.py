import graphene

from .mutations.create import CreatePlan
from .mutations.update import UpdatePlan
from .mutations.delete import DeletePlan


class Mutation(graphene.ObjectType):
    create_plan = CreatePlan.Field()
    update_plan = UpdatePlan.Field()
    delete_plan = DeletePlan.Field()
