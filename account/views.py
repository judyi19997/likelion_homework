from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm #로그인 관련 form
from django.contrib.auth.forms import UserCreationForm #회원가입 관련 form
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def make_login(request):
    if request.method == "POST": #정보 입력 완료 후 상태.
        complete_form = AuthenticationForm(request = request, data = request.POST)
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


    else: #막 페이지 들어간 상태
        login_form = AuthenticationForm()
        return render(request, 'login.html', {'new_form' : login_form})

def make_logout(request):
    logout(request)
    return redirect('begin')


def make_register(request):
    
    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        user = register_form.save()
        return redirect ('begin')
    else:
        new_form = UserCreationForm()
        return render (request, 'login.html', {'new_form':new_form})

