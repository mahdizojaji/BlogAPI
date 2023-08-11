from abc import ABCMeta, abstractmethod
from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractModelMeta(ABCMeta, type(models.Model)):
    pass


class BaseModel(models.Model, metaclass=AbstractModelMeta):
    id = models.AutoField(
        verbose_name=_("ID"),
        primary_key=True,
    )
    uuid = models.UUIDField(
        verbose_name=_("UUID"), unique=True, db_index=True, default=uuid4
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created Time"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated Time"),
        auto_now=True,
    )

    @abstractmethod
    def __str__(self):
        ...

    class Meta:
        abstract = True
