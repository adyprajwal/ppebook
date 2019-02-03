from django.urls import path
from . views import usersList


urlpatterns = [
path('users/', usersList.as_view()),
]