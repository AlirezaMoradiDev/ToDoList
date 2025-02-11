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
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = user
            task.save()
            return redirect('task:list')
    else:
        form = TaskForm()
    return render(request, 'task/add.html', context={'user': user, 'form': form})


@login_required
def detail_task(request, slug):
    task = Task.objects.get(slug=slug)
    task.view += 1
    task.save()
    return render(request, 'task/detail.html', context={'task': task})
