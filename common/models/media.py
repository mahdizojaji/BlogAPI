from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _

from ..utils import get_mime_type_of_file
from .base import BaseModel


class Media(BaseModel):
    uuid = models.UUIDField(
        verbose_name=_("UUID"),
        unique=True,
        default=uuid4,
        db_index=True,
    )
    file = models.FileField(
        verbose_name=_("File"),
    )
    mime_type = models.CharField(
        verbose_name=_("MIME type"),
        null=True,
        blank=True,
        max_length=255,
    )
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
    )

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        if self.file.seekable():
            self.file.seek(0)
        self.mime_type = get_mime_type_of_file(self.file.read())
        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )

    def __str__(self) -> str:
        return f"{self.mime_type} ({self.uuid})"

    class Meta:
        verbose_name = _("Medium")
        verbose_name_plural = _("Media")
