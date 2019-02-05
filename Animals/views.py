
from django.shortcuts import render
from rest_framework import viewsets
from .models import animal
from .serializers import animalSerializer

# Create your views here.
class AnimalView(viewsets.ModelViewSet):
	queryset = animal.objects.all()
	serializer_class = animalSerializer