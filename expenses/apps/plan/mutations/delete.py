import graphene
from graphql import GraphQLError
from graphql_jwt.decorators import login_required

from expenses.utils.messages import plan_response


class DeletePlan(graphene.Mutation):

    message = graphene.String()
    failed = graphene.List(graphene.UUID)

    class Arguments:
        ids = graphene.List(graphene.UUID, required=True)

    @login_required
    def mutate(self, info, **kwargs):
        failed = []
        for id in kwargs.get('ids'):
            try:
                info.context.user.plan_set.get(id=id).delete()
            except Exception:
                failed.append(id)

        # will be equal to 0 if none has been deleted
        difference = len(kwargs.get('ids'))-len(failed)

        if difference:
            message = plan_response.SUCCESS["deleted"].format(difference)
            return DeletePlan(message=message, failed=failed)

        raise GraphQLError(plan_response.ERROR["delete_failed"])
