from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('main tab')


def categories(request, category_id):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{category_id}<p/>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

