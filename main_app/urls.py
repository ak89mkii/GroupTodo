from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('todo/create/', views.CreateTodo.as_view(), name='create_todo'),
    path('todo/<int:pk>/delete/', views.DeleteTodo.as_view(), name='delete_todo')

]