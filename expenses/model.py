from django.db import models
from django.utils import timezone
import uuid

from .manager import SoftDeleteManager


class SoftDeleteModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    objects = SoftDeleteManager()
    all_objects = SoftDeleteManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(SoftDeleteModel, self).delete()
