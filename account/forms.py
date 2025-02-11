from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import request
from django.forms import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "class": "input-field",
        'label': 'Enter your email'
    }))

    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-field',
        'type': 'password',
        'label': 'Enter your password'
    }))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            raise ValidationError('This user is not registered.', code='unregistered')
        else:
            return super().clean()


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class RegisterUserForm(forms.ModelForm):
    password = forms.CharField()
    password_confirm = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('password_confirm')

        if password != confirm:
            raise ValidationError('password and confirm not equal')

