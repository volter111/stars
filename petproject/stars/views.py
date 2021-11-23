from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
        ]


def index(request):

    posts = Celebrities.objects.all()  # получаем все записи с бд, модель Celebrity

    context = {
        'menu': menu,
        'title': 'Домашнаяя страница',
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, 'stars/index.html', context=context)


def about(request):
    return render(request, 'stars/about.html', {'menu': menu, 'title': 'О сайте'})


def add_page(request):
    return HttpResponse("Add page")


def login(request):
    return HttpResponse("Login page")


def contact(request):
    return HttpResponse("Contact us")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def show_post(request, post_slug):
    post = get_object_or_404(Celebrities, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'stars/post.html', context=context)


def show_category(request, cat_id):
    posts = Celebrities.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'posts': posts,
        'cat_selected': cat_id,
    }
    return render(request, 'stars/index.html', context=context)
