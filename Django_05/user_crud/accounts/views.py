from ast import Pass
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login # 실제 세션 데이터를 만들어주는 함수 import
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm, CustomUserChangeForm

 
# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST': # 사람을 실제 로그인을 시켜주는 파트
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 실제 로그인 (주의:save가 아님, 세션을 만듦)
            auth_login(request, form.get_user()) # 이 인증된 유저 정보를 어디서 들고올 것인가?
            return redirect(request.GET.get('next') or 'articles:index') # 단축 평가

    else:# 로그인할 form 보여줌
        form = AuthenticationForm()
        # 이 form을 페이지에 렌더링해야 함
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    # 로그아웃 진행
    auth_logout(request) # 인자는 request만 들어감
    # 로그아웃하면 어디로 리다이렉트?
    return redirect('articles:index')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # save는 객체를 뱉어내고 저장된 객체를 return하고 그게 user정보다
            # 회원가입 후 로그인 상태 유지
            auth_login(request, user)
            return redirect('articles:index') ## 하고 나면 메인페이지로 감
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')


def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)