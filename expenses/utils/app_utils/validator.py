import re
from graphql import GraphQLError
from expenses.apps.authentication.models import User
from django.db.models import Q

from expenses.utils.messages.authentication_response import AUTH_ERROR
from .responses import error
from expenses.utils.messages.expense_response import ERROR


class Validator:
    """
    All validations of fields within the system

    fields:
        validate_password(str): password
    """

    def validate_password(self, password):
        """
        Validate password
        Args:
            password(str): the user's password
        returns:
            password(str): the sent password if it's correct
            error(GraphQLError): if the password is not valid
        """
        self.password = password.strip()
        regex = re.match('(?=.{8,100})(?=.*[A-Z])(?=.*[0-9])', self.password)
        if regex is None:
            raise GraphQLError(AUTH_ERROR["invalid_password"])
        return self.password

    @classmethod
    def validate_user(self, **kwargs):
        """
        Validate user's email and username
        Args:
            username(str): the user's username
            email(str): the user's email
        returns:
            error(GraphQLError): if the email or username is already used
        """
        email = kwargs.get("email")
        username = kwargs.get("username")
        users = User.objects.filter(Q(username=username) | Q(email=email))
        if email in [user.email for user in users]:
            error.used_email_or_username("email", email)
        elif username in [user.username for user in users]:
            error.used_email_or_username("username", username)

    def validate_min_amount(self, value):
        """
        Validate expense minimum value
        Args:
            value(int): the expense amount
        returns:
            error(GraphQLError): if value is less than 1
        """
        if value < 1:
            raise GraphQLError(ERROR["less_amount"])


validator = Validator()
