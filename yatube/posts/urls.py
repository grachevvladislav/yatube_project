from . import views
from django.urls import path

urlpatterns = [
    # Главная страница
    path('index.html', views.index),
    path('', views.index),
    path('group_list.html', views.group_posts),
]
