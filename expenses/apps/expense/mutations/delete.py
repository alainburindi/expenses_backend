import graphene
from graphql_jwt.decorators import login_required
from graphql import GraphQLError

from expenses.utils.messages.expense_response import SUCCESS, ERROR


class DeleteExpense(graphene.Mutation):

    message = graphene.String()
    failed = graphene.List(graphene.UUID)

    class Arguments:
        expenses_id = graphene.List(graphene.UUID, required=True)

    @login_required
    def mutate(self, info, **kwargs):
        expense_ids = kwargs.get('expenses_id')
        failed = []
        for id in expense_ids:
            try:
                info.context.user.expense_set.get(id=id).delete()
            except Exception:
                # if the expense is not found or belongs to someone else
                failed.append(id)

        # will be equal to 0 if none has been deleted
        difference = len(expense_ids)-len(failed)

        if difference:
            message = SUCCESS["deleted"].format(difference)
            return DeleteExpense(message=message, failed=failed)

        raise GraphQLError(ERROR["delete_failed"])
