
from django.shortcuts import render
from rest_framework import viewsets
from . models import Animal
from . serializers import animalSerializer

# Create your views here.
class AnimalView(viewsets.ModelViewSet):
	queryset = Animal.objects.all()
	serializer_class = animalSerializer