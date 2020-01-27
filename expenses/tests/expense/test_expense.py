from ..base_config import TestConfig
from ..test_fixtures.expense import create_expense
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
