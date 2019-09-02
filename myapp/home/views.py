from django.shortcuts import render, redirect
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
            post = form.save(commit=False)
            post.save()
            return redirect('index')
        return render(request, 'createTodo.html')
    else:
        form = TodoForm()
        return render(request, 'createTodo.html', {'form':form})
