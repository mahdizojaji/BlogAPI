from rest_framework import serializers

from common.models import Media
from common.serializers import MediaSerializer

from ..models import Article


class _BaseArticleSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["attachments"] = MediaSerializer(
            instance.attachments.all(), many=True
        ).data
        return representation

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


class ArticleSerializer(_BaseArticleSerializer):
    pass


class ArticleUpdateSerializer(_BaseArticleSerializer):
    attachments = serializers.ListField(write_only=True)

    def update(self, instance: Article, validated_data):
        attachments = validated_data.pop("attachments", [])
        for attachment in attachments:
            media = Media.objects.get(uuid=attachment)
            instance.attachments.add(media)
        return super().update(instance, validated_data)
