from django.urls import path
from . import views

app_name = 'ticket'
urlpatterns = [
    path('add', views.add_ticket, name='add'),
    path('list', views.list_ticket, name='list'),
    path('api', views.list_ticket_api, name='api'),
    path('api/add', views.AddTicket.as_view(), name='add api'),
]
