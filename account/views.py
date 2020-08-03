from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm #로그인 관련 form
from django.contrib.auth.forms import UserCreationForm #회원가입 관련 form
from django.contrib.auth.forms import UserChangeForm #유저정부 수정 관련 form
from django.contrib.auth import login, authenticate, logout
from .forms import loginForm, registerForm, changeForm
from django.contrib import messages


# Create your views here.
def make_login(request):
    if request.method == "POST": #정보 입력 완료 후 상태.
        complete_form = loginForm(request = request, data = request.POST)
        # if complete_form.is_valid():
        #     complete_form.save()
        #     user = authenticate(request = request)
        #     return redirect ("begin")
        if complete_form.is_valid(): #유효하다면?
            user_id = complete_form.cleaned_data['username']
            user_pw = complete_form.cleaned_data['password']
            user = authenticate(request = request, username = user_id, password = user_pw)
            if user is not None: #user가 잘 만들어진거면
                login(request, user)
                return redirect('begin')
        else:
            messages.error(request,"ID와 PW를 다시 확인해주세요.")
            return redirect('login')


    else: #막 페이지 들어간 상태
        login_form = loginForm()
        return render(request, 'login.html', {'new_form' : login_form})

def make_logout(request):
    logout(request)
    return redirect('begin')


def make_register(request):
    if request.method == 'POST':
        register_form = registerForm(request.POST)
        user = register_form.save()
        return redirect ('begin')
    else:
        new_form = registerForm()
        return render (request, 'login.html', {'new_form':new_form})

def make_change(request):
    # unchanged_form = get_object_or_404(changeForm, pk = change)

    if request.method =='POST': #다 끝난 후 제출할때
        change_form = changeForm(request.POST, instance = request.user)
        if change_form.is_valid():
            user = change_form.save()
            return redirect('begin')
    else:
        newChange_form = changeForm(instance = request.user)
        return render (request,'login.html',{'new_form':newChange_form})


