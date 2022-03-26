from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    context = {
        'title': title,
    }
    return render(request, template, context)


def group_posts(request):
    title = 'Лев Толстой – зеркало русской революции.'
    context = {
        'title': title,
    }
    template = 'posts/group_list.html'
    return render(request, template, context)


#def posts(request, any_slug):
#    return HttpResponse(f'Пост про: {any_slug}. В котором интересно рассказано про: {any_slug}')