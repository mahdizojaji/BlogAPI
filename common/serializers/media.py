from rest_framework import serializers

from ..models import Media


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = (
            "uuid",
            "file",
            "mime_type",
            "description",
            "created_at",
        )
        read_only_fields = (
            "uuid",
            "file_url",
            "mime_type",
            "created_at",
        )
