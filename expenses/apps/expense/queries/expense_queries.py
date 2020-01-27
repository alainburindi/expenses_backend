import graphene
from graphql_jwt.decorators import login_required


from ..types import ExpenseType


class Query(graphene.ObjectType):

    my_expenses = graphene.List(ExpenseType)

    @login_required
    def resolve_my_expenses(self, info):
        return info.context.user.expense_set.all()
