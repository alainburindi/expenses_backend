import json
from django.test import TestCase, Client
from expenses.apps.authentication.models import User
from expenses.tests.test_fixtures.authentication import (
    login_user
)
from expenses.apps.expense.models import Expense


class TestConfig(TestCase):
    """
    Test configuration
    """
    @classmethod
    def setUpClass(cls):

        # We need to first run setUpClass function that we
        # inherited from TestCase.
        super(TestConfig, cls).setUpClass()

        # Set up test client for all test classes
        # that will inherit from this class.
        cls.client = Client()

    @classmethod
    def query(cls, query: str = None):
        # Method to run all queries and mutations for tests.
        body = dict()
        body['query'] = query
        response = cls.client.post(
            '/expenses/', json.dumps(body), content_type='application/json')
        json_response = json.loads(response.content.decode())
        return json_response

    @classmethod
    def query_with_token(cls, access_token, query: str = None):
        # Method to run queries and mutations using a logged in user
        # with an authentication token
        body = dict()
        body['query'] = query
        http_auth = 'JWT {}'.format(access_token)
        url = '/expenses/'
        content_type = 'application/json'

        response = cls.client.post(
            url,
            json.dumps(body),
            HTTP_AUTHORIZATION=http_auth,
            content_type=content_type)
        json_response = json.loads(response.content.decode())
        return json_response

    def setUp(self):
        self.default_user_data = {
            "email": "alain@expenses.com",
            "username": "Alainb", "password": "Password123"
        }

        self.second_user_data = {
            "email": "second@expenses.com",
            "username": "Second", "password": "Password123"
        }

        self.default_user = self.register_user(self.default_user_data)
        self.access_token = self.login_user(self.default_user_data)
        self.expense = self.create_expense(self.default_user)
        self.second_user = self.register_user(self.second_user_data)
        self.second_user_expense = self.create_expense(self.second_user)
        self.second_user_access_token = self.login_user(self.second_user_data)

    def register_user(self, user):
        """
        register a new user
        """
        # email = user["email"]
        # mobile_number = user["mobile_number"]
        # password = user["password"]
        user = User.objects.create_user(**user)
        user.is_active = True
        user.save()
        return user

    def login_user(self, user):
        response = self.query(login_user.format(**user))
        return response['data']['loginUser']['authToken']

    def create_expense(self, user):
        return Expense.objects.create(name="test", amount=200,
                                      user=user)
