
from django.shortcuts import render
from rest_framework import viewsets
from .models import color
from .serializers import colorSerializer

# Create your views here.
class ColorView(viewsets.ModelViewSet):
	queryset = color.objects.all()
	serializer_class = colorSerializer