from rest_framework.routers import SimpleRouter

from .views import ArticleViewSet

router = SimpleRouter()
router.register("api/article", ArticleViewSet, basename="media")

urlpatterns = [] + router.urls
