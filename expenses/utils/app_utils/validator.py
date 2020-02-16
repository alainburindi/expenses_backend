import re
from graphql import GraphQLError
from expenses.apps.authentication.models import User
from django.db.models import Q
import datetime

from expenses.utils.messages.authentication_response import AUTH_ERROR
from .responses import error
from expenses.utils.messages.expense_response import ERROR
from expenses.utils.messages import plan_response


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

    def validate_min_amount(self, kwargs):
        """
        Validate amount minimum value
        Args:
            kwargs(dict): containing the request data
        returns:
            error(GraphQLError): if amount is less than 1
        """

        amount = kwargs.get('amount') or 1

        if amount < 1:
            raise GraphQLError(ERROR["less_amount"])

    def valide_plan_due_date(self, kwargs):
        """
        Validate plan due date
        Args:
            kwargs(dict): containing the request data
        returns:
            error(GraphQLError): if due date has already passed
        """
        today = datetime.datetime.today().date()
        due_date = kwargs.get('due_date') or today
        if due_date < today:
            raise GraphQLError(plan_response.ERROR["passed_due_date"])


validator = Validator()
