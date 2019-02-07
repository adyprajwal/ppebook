
from django.shortcuts import render
from rest_framework import viewsets
from .models import Color
from .serializers import colorSerializer

# Create your views here.
class ColorView(viewsets.ModelViewSet):
	queryset = Color.objects.all()
	serializer_class = colorSerializer
	lookup_field = 'color_name'