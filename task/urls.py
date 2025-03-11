from django.urls import path
from . import views


app_name = 'task'
urlpatterns = [
    path('list', views.list_task, name='list'),
    path('add', views.add_task, name='add'),
    path('change_status/<int:id>', views.change_status, name='change status'),
    path('tasks/<int:id>', views.detail_task, name='detail'),
    path('tasks/edit/<int:id>', views.edit_task, name='edit')
]
