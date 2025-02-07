from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import LoginForm


def login_user(request):
    if request.user.is_authenticated:
        return redirect('task:list')
    else:
        print('start')
        if request.method == "POST":
            print('POST')
            form = LoginForm(request.POST)
            if form.is_valid():
                print('1')
                user = User.objects.get(username=form.cleaned_data.get('username'))
                login(request, user)
                print('ok')
                return redirect('task:list')
        else:
            form = LoginForm()
    return render(request, 'account/login.html', context={'form': form})


def register_user(request):
    pass


def logout_user(request):
    logout(request)
    return redirect('home:main')
