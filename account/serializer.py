from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    firstname = serializers.CharField(max_length=60)
    lastname = serializers.CharField(max_length=70)
    username = serializers.CharField(max_length=15)
    email = serializers.EmailField(max_length=255)
