from graphene_django import DjangoObjectType

from .models import Expense


class ExpenseType(DjangoObjectType):
    class Meta:
        model = Expense
