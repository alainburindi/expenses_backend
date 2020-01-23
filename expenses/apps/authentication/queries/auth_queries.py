import graphene
from graphql import GraphQLError

from expenses.utils.messages.authentication_response import AUTH_ERROR
from ..types import UserType


class Query(graphene.ObjectType):

    me = graphene.Field(UserType)

    def resolve_me(self, info):
        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError(AUTH_ERROR["not_logged_in"])

        return user
