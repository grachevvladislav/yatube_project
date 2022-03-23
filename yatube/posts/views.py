from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    return render(request, template)


def group_posts(request):
    template = 'posts/group_list.html'
    return render(request, template)


#def posts(request, any_slug):
#    return HttpResponse(f'Пост про: {any_slug}. В котором интересно рассказано про: {any_slug}')