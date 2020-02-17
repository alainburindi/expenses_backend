import graphene
from graphql_jwt.decorators import login_required

from ..types import PlanType
from expenses.utils.app_utils.validator import validator
from ..models import Plan
from expenses.utils.messages.plan_response import SUCCESS


class CreatePlan(graphene.Mutation):
    plan = graphene.Field(PlanType)
    message = graphene.String()

    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()
        amount = graphene.Int(required=True)
        due_date = graphene.Date(required=True, )

    @login_required
    def mutate(self, info, **kwargs):
        validator.validate_min_amount(kwargs)
        validator.valide_plan_due_date(kwargs)
        plan = Plan(
            user=info.context.user
        )
        for arg in kwargs:
            setattr(plan, arg, kwargs[arg])
        plan.save()

        return CreatePlan(message=SUCCESS["created"], plan=plan)
