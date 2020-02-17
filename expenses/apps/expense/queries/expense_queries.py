import graphene
from graphql_jwt.decorators import login_required


from ..types import ExpenseType


class Query(graphene.ObjectType):

    my_expenses = graphene.List(ExpenseType, search=graphene.String())

    @login_required
    def resolve_my_expenses(self, info, **kwargs):
        search = kwargs.get('search')
        user_expenses = info.context.user.expense_set
        return user_expenses.filter(name__icontains=search) \
            if search else user_expenses.all()
