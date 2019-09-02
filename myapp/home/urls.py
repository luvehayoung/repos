from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name = 'index'),
    path('todo/create', views.createTodo, name = 'createTodo'),
]
