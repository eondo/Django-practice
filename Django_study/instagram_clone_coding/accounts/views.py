from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from .forms import CustomUserCreationForm

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('posts:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('accounts:login')


def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def delete(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            request.user.delete()
            auth_logout(request)
            return redirect('posts:index')
        else:
            return render(request, 'accounts/delete.html')
    return redirect('accounts:login')


def update(request):
    if request.method == 'POST':
        pass
    else:
        pass
