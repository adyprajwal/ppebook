from django.urls import path
from . views import numberList

urlpatterns = [
path('number/', numberList.as_view()),
]