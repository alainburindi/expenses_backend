import graphene
import graphql_jwt

from expenses.apps.authentication import schema as auth_schema
from expenses.apps.authentication.queries import auth_queries
from expenses.apps.expense import schema as expense_schema
from expenses.apps.expense.queries import expense_queries


class Query(auth_queries.Query, expense_queries.Query, graphene.ObjectType):
    pass


class Mutation(
    auth_schema.Mutation, expense_schema.Mutation, graphene.ObjectType
):
    token_auth = graphql_jwt.ObtainJSONWebToken().Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
