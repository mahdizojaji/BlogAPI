from django.contrib.sites.admin import admin

from ..models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
