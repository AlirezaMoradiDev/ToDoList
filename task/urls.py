from django.urls import path
from . import views


app_name = 'task'
urlpatterns = [
    path('list', views.list_task, name='list'),
    path('add', views.add_task, name='add'),
    path('change_status/<slug:slug>', views.change_status, name='change status'),
    path('tasks/<slug:slug>', views.detail_task, name='detail'),
    path('tasks/edit/<slug:slug>', views.edit_task, name='edit')
]
