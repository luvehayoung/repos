from django.shortcuts import render, redirect, get_object_or_404
from myapp.user.models import Todo
from myapp.user.forms import TodoForm
# Create your views here.
def index(request):
    todo = Todo.objects.order_by('created_at').reverse()
    return render(request, 'index.html', {'todos':todo})

def createTodo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('index')
        return render(request, 'createTodo.html')
    else:
        form = TodoForm()
        return render(request, 'createTodo.html', {'form':form})

def viewTodo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'viewTodo.html', {'todo':todo})

def editTodo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo = form.save()
            return redirect('viewTodo', pk=todo.pk)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'createTodo.html', {'form':form})

def deleteTodo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('index')

def doneTodo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.status = "done"
    todo.save()
    return redirect('index')

def backTodo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.status = "on process"
    todo.save()
    return redirect('index')
