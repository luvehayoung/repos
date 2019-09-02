from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name = 'index'),
    path('todo/create', views.createTodo, name = 'createTodo'),
    path('todo/view/<int:pk>', views.viewTodo, name = 'viewTodo'),
    path('todo/edit/<int:pk>', views.editTodo, name='editTodo'),
    path('todo/delete/<int:pk>', views.deleteTodo, name='deleteTodo'),
    path('todo/done/<int:pk>', views.doneTodo, name='doneTodo'),
    path('todo/back/<int:pk>', views.backTodo, name='backTodo'),
]
