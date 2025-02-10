from django.urls import path
from . import views


app_name = 'task'
urlpatterns = [
    path('list', views.list_task, name='list'),
    path('add', views.add_task, name='add'),
    path('tasks/<slug:slug>', views.detail_task, name='detail')
]
