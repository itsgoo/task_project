from django.urls import path, include
from rest_framework import routers
from .views import MainViewSet


router = routers.DefaultRouter()
router.register('', MainViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 