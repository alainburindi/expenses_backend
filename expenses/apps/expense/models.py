from django.db import models
import uuid

from expenses.apps.authentication.models import User
# Create your models here.


class Expense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, max_length=100)
    amount = models.IntegerField(null=False)
    description = models.CharField(null=True, max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
