from uuid import uuid1

from django.db import models
from django.conf import settings


class UUIDPrimaryKeyMixin(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, editable=False, default=uuid1)


class SlugPrimaryKeyMixin(models.Model):
    class Meta:
        abstract = True

    id = models.CharField(primary_key=True, max_length=128)


class OwnerMixin(models.Model):
    class Meta:
        abstract = True

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)
