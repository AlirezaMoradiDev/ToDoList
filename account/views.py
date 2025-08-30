from django.contrib.auth import login, logout
from .models import MyUser
from django.shortcuts import render, redirect
from .forms import LoginForm, EditProfileForm, RegisterUserForm
from rest_framework.decorators import api_view
from .serializer import UserSerializer
from rest_framework.response import Response


def login_user(request):
    if request.user.is_authenticated:
        return redirect('task:list')
    else:
        print('start')
        if request.method == "POST":
            print('POST')
            form = LoginForm(request.POST)
            if form.is_valid():
                user = MyUser.objects.get(username=form.cleaned_data.get('username'))
                login(request, user)
                return redirect('task:list')
        else:
            form = LoginForm()
    return render(request, 'account/login.html', context={'form': form})


def register_user(request):
    if request.user.is_authenticated:
        return redirect('task:list')
    else:
        if request.method == "POST":
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                password = form.cleaned_data.get('password')
                user.set_password(password)
                user.save()
                login(request, user)
                return redirect('home:main')
        else:
            form = RegisterUserForm()
    return render(request, 'account/register.html', context={'form': form})


def logout_user(request):
    logout(request)
    return redirect('home:main')


def edit_user(request):
    user = request.user
    if request.method == "POST":
        form = EditProfileForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('task:list')
    else:
        form = EditProfileForm(instance=user)
    return render(request, 'account/edit.html', context={'form': form})

@api_view(['GET'])
def user_api(request):
    users = MyUser.objects.all()
    ser = UserSerializer(instance=users, many=True)
    return Response(ser.data)
