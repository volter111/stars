from django.urls import path
from stars.views import *

urlpatterns = [
    path('', index),
    path('categories/', categories),
]
