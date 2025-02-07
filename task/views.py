from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


@login_required
def list_task(request):
    user = request.user
    tasks = Task.objects.filter(user=user)
    return render(request, 'task/list.html', context={'tasks': tasks, 'user': user})


@login_required
def add_task(request):
    user = request.user
    if request.method == "POST":
        form = TaskForm(request.POST, user=user)
        if form.is_valid():
            form.save()
            return redirect('task:list')
    else:
        form = TaskForm()
    return render(request, 'task/add.html', context={'user': user, 'form': form})

