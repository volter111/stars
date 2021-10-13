from django.urls import path, include
from stars.views import *

urlpatterns = [
    path('', index),
    path('categories/', categories),
]