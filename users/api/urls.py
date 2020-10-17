from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProfileViewSet


# Define URLs, and corresponding viewsets using DRF routers
router = DefaultRouter()

router.register(r"users", UserViewSet)
router.register(r"profiles", ProfileViewSet)

urlpatterns = [
    path("", include(router.urls))
]
