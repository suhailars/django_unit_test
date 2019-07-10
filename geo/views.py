import json
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import Http404
from geo.geo_api import get_address
from geo.models import Geo
from django.utils import timezone



class GeoView(APIView):
    """
    get address.
    """
    permission_classes = (AllowAny,)

    def get(self, request, lat, lon, format=None):
    	
        try:
        	geo_info = Geo.objects.get(lat=lat, lon=lon)
        	date = geo_info.date
        	current_date = timezone.now()
        	diff = current_date - date
        	days = diff.days
        except Geo.DoesNotExist:
        	geo_info = ""
        	days = 0
        if not geo_info:
        	address = get_address(lat, lon)
        	geo_info = Geo.objects.create(lat=lat, lon=lon, place=address)
        elif days > 0:
        	address = get_address(lat, lon)
        	geo_info.place = address
        	geo_info.save()

        return Response({"name" : geo_info.place})
