import graphene
from graphql_jwt.decorators import login_required
from graphql import GraphQLError

from ..types import ExpenseType
from ..models import Expense
from expenses.utils.app_utils.validator import validator
from expenses.utils.messages.expense_response import SUCCESS, ERROR


class UpdateExpense(graphene.Mutation):
    updated = graphene.Field(ExpenseType)
    message = graphene.String()

    class Arguments:
        id = graphene.UUID(required=True)
        name = graphene.String()
        description = graphene.String()
        amount = graphene.Int()

    @login_required
    def mutate(self, info, **kwargs):
        validator.validate_min_amount(kwargs)

        expense = Expense.objects.get(id=kwargs.get('id'))
        if expense.user != info.context.user:
            raise GraphQLError(ERROR["not_owner"])

        for arg in kwargs:
            setattr(expense, arg, kwargs[arg])
        expense.save()
        return UpdateExpense(updated=expense, message=SUCCESS["updated"])
