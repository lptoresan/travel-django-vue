from rest_framework import viewsets
from travel.api import serializers
from travel import models

class TravelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TravelSerializers
    queryset = models.Travel.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UsersSerializer
    queryset = models.Users.objects.all()