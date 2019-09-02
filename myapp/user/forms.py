from django import forms
from .models import Todo

class DateInput(forms.DateInput):
    input_type = 'date'
    
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'content', 'due_date')
        widgets = {
            'due_date': DateInput(attrs={'type': 'date'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
