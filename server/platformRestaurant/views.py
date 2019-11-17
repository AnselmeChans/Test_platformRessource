from rest_framework import viewsets
from django.shortcuts import render

from .models import User, Room, Info
from .serializers import UserSerializer, RoomSerialiser, InfoSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class RoomViewSet(viewsets.ModelViewSet):
    '''
    This comment will be visible in the web interface
    '''
    queryset = Room.objects.all()
    serializer_class = Room

class InfoViewSet(viewsets.ModelViewSet):
    '''
    This comment will be visible in the web interface
    '''
    queryset = Info.objects.all()
    serializer_class = Info


