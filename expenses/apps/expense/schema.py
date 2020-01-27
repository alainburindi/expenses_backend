import graphene

from .mutations.create import CreateExpense
from .mutations.update import UpdateExpense


class Mutation(graphene.ObjectType):
    create_expense = CreateExpense.Field()
    update_expense = UpdateExpense.Field()
