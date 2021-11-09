from django.urls import path
from stars.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('categories/<int:category_id>/', categories),
]

handler404 = pageNotFound
