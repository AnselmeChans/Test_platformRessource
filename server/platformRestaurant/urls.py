from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RoomViewSet, InfoViewSet
from django.urls import include, path
from rest_framework import routers
from platformRestaurant.views import *

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('room', RoomViewSet)
router.register('info', InfoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]




