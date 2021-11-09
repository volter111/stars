from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

# Create your views here.

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(request):
    posts = Celebrity.objects.all()  # получаем все записи с бд, модель Celebrity
    return render(request, 'stars/index.html', {'menu': menu, 'title': 'Домашнаяя страница', 'posts': posts})


def about(request):
    return render(request, 'stars/about.html', {'menu': menu, 'title': 'О сайте'})


def categories(request, category_id):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{category_id}<p/>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
