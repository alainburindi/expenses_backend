import graphene
from graphql_jwt.decorators import login_required


from ..types import PlanType


class Query(graphene.ObjectType):

    my_plans = graphene.List(PlanType, search=graphene.String())

    @login_required
    def resolve_my_plans(self, info, **kwargs):
        search = kwargs.get('search')
        user_plans = info.context.user.plan_set.all()
        return user_plans.filter(name__icontains=search) if search else user_plans
