from django.urls import path
from travel.views import TravelIndividual, TravelDetailUpdateDelete, TravelDestination, TravelSearch

urlpatterns = [
    path('', TravelIndividual.as_view()),
    path('<uuid:pk>/', TravelDetailUpdateDelete.as_view()),
    path('city/<str:city>/', TravelDestination.as_view()),
    path('search/', TravelSearch.as_view(), name='travel-search'),
]