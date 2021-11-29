from django.urls import path
from stars.views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_page/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='show_post_page'),
    path('category/<slug:cat_slug>', ShowCategory.as_view(), name='category'),
]

handler404 = pageNotFound
