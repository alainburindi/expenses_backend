from ..base_config import TestConfig
from ..test_fixtures import plan as plan_fixtures
from expenses.utils.messages import plan_response


class TestPlan(TestConfig):
    def test_create_plan(self):
        response = self.query_with_token(
            self.access_token, plan_fixtures.create_plan.format(
                **self.plan_data)
        )
        self.assertEqual(plan_response.SUCCES["created"],
                         response["data"]["createPlan"]["message"])
        self.assertDictContainsSubset(
            response["data"]["createPlan"]["plan"], self.plan_data)

    def test_create_plan_with_passed_due_date(self):
        self.plan_data["dueDate"] = "2020-02-02"
        response = self.query_with_token(
            self.access_token, plan_fixtures.create_plan.format(
                **self.plan_data)
        )
        self.assertEqual(plan_response.ERROR["passed_due_date"],
                         response["errors"][0]["message"])
