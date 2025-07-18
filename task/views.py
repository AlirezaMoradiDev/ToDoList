from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .forms import TaskForm, EditForm
from .models import Task


@login_required
def list_task(request):
    user = request.user
    tasks = Task.objects.filter(user=user)
    paginator = Paginator(tasks, 2)
    page_number = request.GET.get('page')
    object_page = paginator.get_page(page_number)
    count_tasks = Task.customManager.counter_object() # this must refactor
    return render(request, 'task/list.html', context={'tasks': object_page, 'user': user, 'count': count_tasks})


@login_required
@csrf_exempt
def add_task(request):
    user = request.user
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = user
            task.save()
            return redirect('task:list')
    else:
        form = TaskForm()
    return render(request, 'task/add.html', context={'user': user, 'form': form})


@login_required
def detail_task(request, id):
    task = Task.objects.get(id=id)
    task.view += 1
    task.save()
    return render(request, 'task/detail.html', context={'task': task})


@login_required
def edit_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        form = EditForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
    else:
        form = EditForm(instance=task)
    return render(request, 'task/edit.html', context={'form': form, 'task': task})


@login_required
def change_status(request, id):
    task = Task.objects.get(id=id)
    if task.status == 'Not completed':
        task.status = 'completed'
        task.save()
    else:
        task.status = 'Not completed'
        task.save()
    return redirect('task:list')


def delete_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        task.delete()
        return HttpResponseRedirect("/")

    return render(request, "task/delete.html", context={})
