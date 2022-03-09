from . import views
from django.urls import path

urlpatterns = [
    # Главная страница
    path('', views.index),
    path('group/', views.group_posts),
    path('group/<slug:any_slug>/', views.posts),
]