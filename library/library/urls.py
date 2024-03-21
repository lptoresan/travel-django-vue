from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from travel.api import viewsets as travelviewsets

route = routers.DefaultRouter()

route.register(r'travels', travelviewsets.TravelViewSet, basename="Travels")
route.register(r'user', travelviewsets.UserViewSet, basename="User")

# Foram feitas duas opções, uma utilizando as viewsets do rest framework
# E a outra utilizando a APIView também do rest framework
urlpatterns = [
    path('', include(route.urls)),
    path('travel-urls/', include('travel.urls')),
]
