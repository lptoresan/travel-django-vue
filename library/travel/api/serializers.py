from rest_framework import serializers
from travel import models

class TravelSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Travel
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Users
        fields = '__all__'