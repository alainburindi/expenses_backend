from graphql import GraphQLError

from expenses.utils.messages.authentication_response import AUTH_ERROR


class Error:
    def used_email_or_username(self, key, value):
        raise GraphQLError(
            AUTH_ERROR["email_username_in_use"].format(key=key, value=value))


error = Error()
