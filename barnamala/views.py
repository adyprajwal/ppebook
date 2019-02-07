from django.shortcuts import render
from . models import barna
from  rest_framework import viewsets
from . serializers import barnaSerializer

# Create your views here.

class BarnaView(viewsets.ModelViewSet):
	queryset = barna.objects.all()
	serializer_class = barnaSerializer
	lookup_field = 'barna_letter'
