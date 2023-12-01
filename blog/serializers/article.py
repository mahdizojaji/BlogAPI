from rest_framework import serializers

from ..models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            "uuid",
            "title",
            "slug",
            "status",
            "body",
            "attachments",
            "created_at",
            "published_at",
            "archived_at",
        )
        read_only_fields = (
            "uuid",
            "slug",
            "author",
            "status",
            "created_at",
            "published_at",
            "archived_at",
        )
