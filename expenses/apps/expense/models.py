from django.db import models

from expenses.apps.authentication.models import User
from django.core.validators import MinValueValidator
from expenses.model import SoftDeleteModel
from expenses.apps.plan.models import Plan


class Expense(SoftDeleteModel):
    name = models.CharField(null=False, max_length=100)
    amount = models.PositiveIntegerField(
        null=False, validators=[MinValueValidator(1)])
    description = models.CharField(null=True, max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)
