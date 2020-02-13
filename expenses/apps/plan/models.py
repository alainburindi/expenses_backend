from django.db import models
from django.core.validators import MinValueValidator

from expenses.model import SoftDeleteModel
from expenses.apps.authentication.models import User


class Plan(SoftDeleteModel):
    name = models.CharField(null=False, max_length=100)
    amount = models.PositiveIntegerField(
        null=False, validators=[MinValueValidator(1)])
    description = models.CharField(null=True, max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    to_be_done = models.DateTimeField(null=False)
    done_date = models.DateTimeField(blank=True, null=True)
