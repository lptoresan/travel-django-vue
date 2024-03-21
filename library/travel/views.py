from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from travel.models import Travel
from travel.api.serializers import TravelSerializers

class TravelIndividual(APIView):
    def get(self, request):
        travels = Travel.objects.all()
        serializer = TravelSerializers(travels, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = TravelSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TravelDetailUpdateDelete(APIView):
    def get_pk(self, pk):
        try:
            return Travel.objects.get(pk=pk)
        except Travel.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        travel = self.get_pk(pk)
        serializer = TravelSerializers(travel)
        return Response(serializer.data)
    
    def put(self, request, pk):
        travel = self.get_pk(pk)
        serializer = TravelSerializers(travel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        travel = self.get_pk(pk)
        travel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TravelDestination(APIView):
    def get(self, request, city):
        travel = Travel.objects.filter(city=city)
        if not travel:  
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TravelSerializers(travel, many=True)
        return Response(serializer.data)
    
class TravelSearch(APIView):
    def get(self, request):
        params = request.query_params
        filters = {}

        if 'city' in params:
            filters['city'] = params['city']
        if 'name' in params:
            filters['name__icontains'] = params['name']  
        if 'price_confort' in params:
            filters['price_confort__lte'] = params['price_confort'] 
        if 'price_econ' in params:
            filters['price_econ__lte'] = params['price_econ'] 
    
        queryset = Travel.objects.filter(**filters)
    
        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        serializer = TravelSerializers(queryset, many=True)
        return Response(serializer.data)