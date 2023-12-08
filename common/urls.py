from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import MediaViewSet, RegisterAPIView

router = SimpleRouter()
router.register("api/media", MediaViewSet, basename="media")

urlpatterns = [
    path("api/auth/register/", RegisterAPIView.as_view(), name="auth-register"),
    path("api/auth/login/", TokenObtainPairView.as_view(), name="auth-login"),
    path(
        "api/auth/refresh-token/", TokenRefreshView.as_view(), name="auth-token-refresh"
    ),
    path("api/auth/verify-token/", TokenVerifyView.as_view(), name="auth-token-verify"),
] + router.urls
