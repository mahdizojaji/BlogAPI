from django.contrib.sites.admin import admin

from ..models import Media


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    pass
