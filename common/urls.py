from rest_framework.routers import SimpleRouter

from .views import MediaViewSet

router = SimpleRouter()
router.register("api/media", MediaViewSet, basename="media")

urlpatterns = [] + router.urls
