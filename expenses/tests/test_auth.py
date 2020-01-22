from expenses.tests.base_config import TestConfig
from expenses.tests.test_fixtures.authentication import (
    create_user, login_user, login_empty_email_and_username
)
from expenses.utils.messages.authentication_response import (
    AUTH_SUCCESS, AUTH_ERROR
)


class TestAuth(TestConfig):

    def setUp(self):
        super(TestAuth, self).setUp()
        self.user = {"email": "alainsecond@expenses.com",
                     "username": "Alainsecond", "password": "Password123"}

    def test_signup(self):
        response = self.query(create_user.format(**self.user))
        self.assertEqual(AUTH_SUCCESS["created"],
                         response["data"]["createUser"]["message"])
        self.assertDictContainsSubset(
            response["data"]["createUser"]["user"], self.user)
        # used email
        response = self.query(create_user.format(**self.user))
        self.assertEqual(AUTH_ERROR["email_username_in_use"].format(
            key="email", value=self.user["email"]),
            response["errors"][0]["message"]
        )

    def test_duplicate_username(self):
        self.default_user_data['email'] = "unusedemail@expenses.com"
        response = self.query(create_user.format(**self.default_user_data))
        self.assertEqual(AUTH_ERROR["email_username_in_use"].format(
            key="username", value=self.default_user_data["username"]),
            response["errors"][0]["message"]
        )

    def test_invalid_password(self):
        self.user["password"] = "invalid"
        response = self.query(create_user.format(**self.user))
        self.assertEqual(AUTH_ERROR["invalid_password"],
                         response["errors"][0]["message"])

    def test_login(self):
        response = self.query(login_user.format(**self.default_user_data))
        self.assertEqual(AUTH_SUCCESS["success_login"],
                         response['data']['loginUser']['message'])

    def test_empty_username_and_email(self):
        response = self.query(login_empty_email_and_username)
        self.assertEqual(AUTH_ERROR['invalid_credentials'],
                         response['errors'][0]['message'])

    def test_login_invalid_password(self):
        self.default_user_data["password"] = "wrongPassword"
        response = self.query(login_user.format(**self.default_user_data))
        self.assertEqual(AUTH_ERROR['invalid_credentials'],
                         response['errors'][0]['message'])

    def test_unexisting_user(self):
        response = self.query(login_user.format(**self.user))
        self.assertEqual(AUTH_ERROR['invalid_credentials'],
                         response['errors'][0]['message'])
