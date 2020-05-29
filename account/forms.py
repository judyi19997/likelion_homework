from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm #기본 form들
from django.contrib.auth import get_user_model
# from .models import custom_model - 비효율적

user = get_user_model()

class loginForm(AuthenticationForm):
    pass

class registerForm(UserCreationForm):

    class Meta:
        model = user
        fields = ['username', 'password1','password2','email','birthday','gender']