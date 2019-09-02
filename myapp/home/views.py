from django.shortcuts import render
from myapp.user.models import Todo
# Create your views here.
def index(request):
    todo = Todo.objects.order_by('created_at').reverse()
    return render(request, 'index.html', {'todos':todo})
