from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.views.generic import ListView
from .forms import TaskForm, EditForm
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework import status

@login_required
def list_task(request):
    user = request.user
    tasks = Task.objects.filter(user=user)
    paginator = Paginator(tasks, 2) # paginator(object, num)
    page_number = request.GET.get('page')
    object_page = paginator.get_page(page_number) # get page
    count_tasks = Task.customManager.counter_object() # this must refactor
    return render(request, 'task/list.html', context={'tasks': object_page, 'user': user, 'count': count_tasks})


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task/list.html'
    paginate_by = 2
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


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

class TaskView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    def get(self, request):
        tasks = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user'] = request.user
            serializer.save()
            return Response({'status': 'added'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


    def patch(self, request, pk):
        try:
            task = Task.objects.get(id=pk)
        except:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(instance=task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors)

    def delete(self, request, pk):
        try:
            task = Task.objects.get(id=pk)
        except:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response({'status': 'deleted'}, status=status.HTTP_204_NO_CONTENT)