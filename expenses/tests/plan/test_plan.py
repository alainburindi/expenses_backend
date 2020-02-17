from ..base_config import TestConfig
from ..test_fixtures import plan as plan_fixtures
from expenses.utils.messages import plan_response


class TestPlan(TestConfig):
    def test_create_plan(self):
        response = self.query_with_token(
            self.access_token, plan_fixtures.create_plan.format(
                **self.plan_data)
        )
        self.assertEqual(plan_response.SUCCESS["created"],
                         response["data"]["createPlan"]["message"])
        self.assertDictContainsSubset(
            response["data"]["createPlan"]["plan"], self.plan_data)

    def test_create_plan_with_passed_due_date(self):
        self.plan_data["due_date"] = "2020-02-02"
        response = self.query_with_token(
            self.access_token, plan_fixtures.create_plan.format(
                **self.plan_data)
        )
        self.assertEqual(plan_response.ERROR["passed_due_date"],
                         response["errors"][0]["message"])

    def test_update_plan(self):
        self.plan_data["name"] = "this is the new name"

        response = self.query_with_token(
            self.access_token, plan_fixtures.update_plan.format(
                id=self.plan.id, **self.plan_data)
        )
        self.assertEqual(self.plan_data["name"],
                         response["data"]["updatePlan"]["plan"]["name"])

    def test_delete_plan(self):
        response = self.query_with_token(
            self.access_token, plan_fixtures.delete.format('["{}"]'.format(
                self.plan.id)
            )
        )
        self.assertEqual(response['data']['deletePlan']['message'],
                         plan_response.SUCCESS['deleted'].format(1))

    def test_delete_someone_plan(self):
        response = self.query_with_token(
            self.second_user_access_token, plan_fixtures.delete.format(
                '["{}"]'.format(self.plan.id))
        )
        self.assertEqual(plan_response.ERROR["delete_failed"],
                         response["errors"][0]["message"])
