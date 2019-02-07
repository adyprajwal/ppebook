from django.shortcuts import render
from rest_framework import viewsets
from .models import Alphabets
from .serializers import AlphaSerializers

# Create your views here.
class AlphaView(viewsets.ModelViewSet):
	queryset = Alphabets.objects.all()
	serializer_class = AlphaSerializers
	lookup_field = 'alpha_letter_lower'