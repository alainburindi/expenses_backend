import graphene
from graphql_jwt.decorators import login_required

from ..types import PlanType
from expenses.utils.app_utils.validator import validator
from expenses.utils.messages.plan_response import SUCCESS


class UpdatePlan(graphene.Mutation):
    plan = graphene.Field(PlanType)
    message = graphene.String()

    class Arguments:
        id = graphene.UUID(required=True)
        description = graphene.String()
        amount = graphene.Int()
        due_date = graphene.Date()
        name = graphene.String()

    @login_required
    def mutate(self, info, **kwargs):

        validator.validate_min_amount(kwargs)
        validator.valide_plan_due_date(kwargs)
        # get the plan from the user's plan set
        plan = info.context.user.plan_set.get(id=kwargs.get('id'))

        for arg in kwargs:
            setattr(plan, arg, kwargs[arg])

        plan.save()

        return UpdatePlan(message=SUCCESS["updated"], plan=plan)
