from . import views
from django.urls import path

app_name = 'posts'


urlpatterns = [
    # Главная страница
    path('', views.index, name='top'),
    path('group_list/', views.group_posts, name='group'),
]
