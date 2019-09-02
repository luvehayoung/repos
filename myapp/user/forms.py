from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'content')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
