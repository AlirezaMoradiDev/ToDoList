from rest_framework import serializers
from .models import Task


# class TaskSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=60)
#     status = serializers.CharField(max_length=30, default='Not completed')
#     created_at = serializers.DateTimeField()

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ("description", "slug", "image")

