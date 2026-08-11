from rest_framework import serializers
from .models import MyUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['firstname', 'username', 'password']
        extra_kwargs = {
            'password':{
                'write_only': True
            },
            'firstname':{
                'read_only' : True
            }
        }


    def create(self, validated_data):
        password =  validated_data.pop('password')
        user = MyUser(**validated_data)
        user.set_password(password)
        user.save()
        return user