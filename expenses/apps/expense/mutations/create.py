import graphene
from graphql_jwt.decorators import login_required

from ..types import ExpenseType
from ..models import Expense
from expenses.utils.app_utils.validator import validator
from expenses.utils.messages.expense_response import SUCCESS


class CreateExpense(graphene.Mutation):
    expense = graphene.Field(ExpenseType)
    message = graphene.String()

    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()
        amount = graphene.Int(required=True)

    @login_required
    def mutate(self, info, **kwargs):
        amount = kwargs.get('amount')
        validator.validate_min_amount(kwargs)
        expense = Expense.objects.create(
            amount=amount,
            name=kwargs.get('name'),
            description=kwargs.get('description'),
            user=info.context.user
        )
        return CreateExpense(expense=expense, message=SUCCESS["created"])
