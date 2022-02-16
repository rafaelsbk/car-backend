from django.urls import path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter
from .views import CarViewSet

router = DefaultRouter()

router.register("car", CarViewSet, basename="car")

urlpatterns = [
    path("", include(router.urls)),
]
