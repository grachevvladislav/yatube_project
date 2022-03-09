from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def groups_list(request):
    return HttpResponse('Список груп')


def posts(request, slug):
    return HttpResponse(f'Пост номер {slug}')