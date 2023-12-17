from rest_framework import serializers

from common.models import Media

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

    def update(self, instance: Article, validated_data):
        attachments = validated_data.pop("attachments", [])
        for attachment in attachments:
            media = Media.objects.get(uuid=attachment)
            instance.attachments.add(media)
        return super().update(instance, validated_data)
