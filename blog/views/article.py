from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication

from ..models import Article
from ..serializers import ArticleSerializer

User = get_user_model()


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTStatelessUserAuthentication]
    serializer_class = ArticleSerializer
    lookup_field = "uuid"

    def get_queryset(self):
        if self.action == "explore":
            return Article.objects.filter(status=Article.Status.PUBLISHED)
        return Article.objects.filter(author_id=self.request.user.id)

    def perform_create(self, serializer):
        user = User.objects.get(id=self.request.user.id)
        serializer.save(author=user)

    @action(
        methods=["GET"], detail=True, url_path="publish", url_name="publish-article"
    )
    def publish_article(self, request, uuid):
        article: Article = self.get_object()
        article.make_publish()
        article.save()
        return Response(ArticleSerializer(article).data)

    @action(
        methods=["GET"], detail=True, url_path="archive", url_name="archive-article"
    )
    def archive_article(self, request, uuid):
        article: Article = self.get_object()
        article.make_archive()
        article.save()
        return Response(ArticleSerializer(article).data)

    @action(methods=["GET"], detail=False, url_path="explore", url_name="explore")
    def explore(self, request):
        return self.list(request)
