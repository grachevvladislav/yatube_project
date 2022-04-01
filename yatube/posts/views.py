from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    #Проверка на наличие такой группы
    group = get_object_or_404(Group, slug=slug)
    #Выбор нужных постов по фильтру
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, template, context)
