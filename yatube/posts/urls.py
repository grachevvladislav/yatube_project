from django.urls import path

from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    path('group/', views.groups_list()),
    path('group/<slug:slug>/', views.posts()),
]