from django.urls import path
from stars.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add_page/', add_page, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>', show_post, name='show_post_page'),
    path('category/<int:cat_id>', show_category, name='category'),
]

handler404 = pageNotFound
