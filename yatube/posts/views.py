from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_posts(request):
    return HttpResponse('Список груп')


def posts(request, any_slug):
    return HttpResponse(f'Пост про: {any_slug}. В котором интересно рассказано про: {any_slug}')