import graphene
from graphql_jwt.decorators import login_required

from ..types import PlanType
from expenses.utils.app_utils.validator import validator
from ..models import Plan
from expenses.utils.messages.plan_response import SUCCES


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
        amount = kwargs.get('amount')
        validator.validate_min_amount(amount)
        due_date = kwargs.get('due_date')
        validator.valide_plan_due_date(due_date)
        plan = Plan.objects.create(
            due_date=due_date,
            amount=amount,
            name=kwargs.get('name'),
            description=kwargs.get('description'),
            user=info.context.user
        )

        return CreatePlan(message=SUCCES["created"], plan=plan)
