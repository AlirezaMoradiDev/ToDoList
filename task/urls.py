from django.urls import path
from . import views


app_name = 'task'
urlpatterns = [
    path('list', views.list_task, name='list')
]
