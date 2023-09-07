import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.constants import MAX_CHAR_FIELD_NAME_LENGTH

User = get_user_model()


def get_sentinel_user():
    return get_user_model().objects.get_or_create(email="deleted")[0]


class UUIDModel(models.Model):
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class CreationTimestampedModel(models.Model):
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
    created_by = models.ForeignKey(
        User,
        verbose_name=_("Created by"),
        on_delete=models.SET(get_sentinel_user),
        null=True,
        related_name="created_%(app_label)s_%(class)s_set",
    )

    class Meta:
        abstract = True


class UpdateTimestampedModel(models.Model):
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True, editable=False)
    updated_by = models.ForeignKey(
        User,
        verbose_name=_("Updated by"),
        on_delete=models.SET(get_sentinel_user),
        null=True,
        related_name="updated_%(app_label)s_%(class)s_set",
    )

    class Meta:
        abstract = True


class TimestampedModel(CreationTimestampedModel, UpdateTimestampedModel):
    class Meta:
        abstract = True


class BaseModel(UUIDModel, TimestampedModel):
    class Meta:
        abstract = True
