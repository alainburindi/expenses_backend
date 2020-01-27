import graphene

from .mutations.create import CreateExpense


class Mutation(graphene.ObjectType):
    create_expense = CreateExpense.Field()
