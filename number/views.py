
from django.shortcuts import render
from rest_framework import viewsets
from .models import numbers
from .serializers import numberSerializer

# Create your views here.
class NumberView(viewsets.ModelViewSet):
	queryset = numbers.objects.all()
	serializer_class = numberSerializer
	lookup_field = 'num_id'