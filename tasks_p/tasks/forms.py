from .models import Task
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание',
            }),
            'deadline': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Рассмотреть до',
            }),
        }
