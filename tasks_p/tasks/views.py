from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):

    data = {
        'title': 'Главная страница',
        'tasks': Task.objects.all(),
    }

    return render(request, 'tasks/index.html', data)


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Ошибка при заполнении формы'

    form = TaskForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'tasks/create.html', data)
