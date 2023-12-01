from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel, Media


class Article(BaseModel):
    class Status(models.TextChoices):
        DRAFT = "draft", _("Draft")
        PUBLISHED = "published", _("Published")
        ARCHIVED = "archived", _("Archived")

    title = models.CharField(
        verbose_name=_("Title"),
        max_length=255,
    )
    slug = models.SlugField(
        verbose_name=_("Slug"),
        max_length=255,
        allow_unicode=True,
    )
    status = models.CharField(
        verbose_name=_("Status"),
        max_length=255,
        choices=Status.choices,
        default=Status.DRAFT,
    )
    body = models.TextField(
        verbose_name=_("Body"),
    )
    attachments = models.ManyToManyField(
        verbose_name=_("Attachments"),
        to=Media,
        related_name="articles",
        blank=True,
    )
    author = models.ForeignKey(
        verbose_name=_("Author"),
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name="articles",
    )
    published_at = models.DateTimeField(
        verbose_name="Published At",
        null=True,
        blank=True,
    )
    archived_at = models.DateTimeField(
        verbose_name="Archived At",
        null=True,
        blank=True,
    )

    def make_archive(self):
        if self.status == self.Status.PUBLISHED:
            self.status = self.Status.ARCHIVED
            self.archived_at = timezone.now()
            self.published_at = None

    def make_publish(self):
        if self.status in [self.Status.DRAFT, self.Status.ARCHIVED]:
            self.status = self.Status.PUBLISHED
            self.published_at = timezone.now()
            self.archived_at = None

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
