from ..base_config import TestConfig
from ..test_fixtures.expense import (
    create_expense, get_my_expenses, update_expense
)
from expenses.utils.messages.expense_response import SUCCESS, ERROR


class TestExpense(TestConfig):

    def test_create_epense(self):
        data = {
            "name": "internet", "amount": 2000
        }
        response = self.query_with_token(
            self.access_token, create_expense.format(**data))
        self.assertEqual(SUCCESS["created"],
                         response['data']['createExpense']['message'])
        self.assertEqual(data, response['data']['createExpense']['expense'])

    def test_incorrect_amount(self):
        data = {
            "name": "internet", "amount": -2
        }
        response = self.query_with_token(
            self.access_token, create_expense.format(**data))
        self.assertEqual(response["errors"][0]
                         ["message"], ERROR["less_amount"])

    def test_get_my_expenses(self):
        response = self.query_with_token(self.access_token, get_my_expenses)
        self.assertIsNotNone(response['data']['myExpenses'])
        self.assertEqual(1, len(response['data']['myExpenses']))

    def test_update_expense(self):
        data = {
            "id": self.expense.id,
            "name": "transport",
            "description": "going to work",
            "amount": 300
        }
        response = self.query_with_token(
            self.access_token, update_expense.format(**data))
        self.assertDictContainsSubset(
            response["data"]["updateExpense"]["updated"], data
        )

    def test_update_someone_expense(self):
        data = {
            "id": self.expense.id,
            "name": "transport",
            "description": "going to work",
            "amount": 300
        }
        response = self.query_with_token(
            self.second_user_access_token, update_expense.format(**data))
        self.assertEqual(response["errors"][0]
                         ["message"], ERROR["not_owner"])
