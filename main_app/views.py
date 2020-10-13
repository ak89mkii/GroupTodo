from django.shortcuts import render
from .models import Todo
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView


# Create your views here.
class Home(ListView):
    model = Todo

class CreateTodo(CreateView):
    model = Todo
    fields = ['name']    

class DeleteTodo(DeleteView):
    model = Todo
    success_url = '/'

# def delete (request, id):
#     todo.objects.get(id=id).delete()
#         return redirect('/')
    