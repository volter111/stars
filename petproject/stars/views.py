from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('main tab')


def categories(request):
    return HttpResponse('categories tab')