import graphene

from .mutations.create import CreateExpense
from .mutations.update import UpdateExpense
from .mutations.delete import DeleteExpense


class Mutation(graphene.ObjectType):
    create_expense = CreateExpense.Field()
    update_expense = UpdateExpense.Field()
    delete_expense = DeleteExpense.Field()
