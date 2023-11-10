from rest_framework import mixins, viewsets

from ..models import Media
from ..serializers import MediaSerializer


class MediaViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()
    lookup_field = "uuid"
