import graphene
from django.core.validators import validate_email

from expenses.utils.app_utils.validator import validator
from expenses.utils.messages.authentication_response import (
    AUTH_SUCCESS
)
from expenses.apps.authentication.types import UserType
from django.contrib.auth import get_user_model
User = get_user_model()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    message = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        email = kwargs.get('email')
        username = kwargs.get('username')
        validate_email(email)
        password = validator.validate_password(password=kwargs.get('password'))
        validator.validate_user(**kwargs)
        user = User(
            username=username,
            email=email,
            is_active=True  # waiting for email verification
        )
        user.set_password(password)
        user.save()

        return CreateUser(
            user=user,
            message=AUTH_SUCCESS["created"]
        )
