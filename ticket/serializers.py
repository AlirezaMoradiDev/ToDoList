from rest_framework import serializers
from .models import Ticket
from account.models import MyUser


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['title', 'user']

