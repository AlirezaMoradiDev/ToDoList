from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Task


#@login_required
def list_task(request):
    #tasks = Task.objects.get(user=request.user)
    return render(request, 'task/list.html', context={})

