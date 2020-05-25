from django import forms
from .models import Blog_m

class Blog_f(forms.ModelForm):
    class Meta:
        model = Blog_m
        fields = ['title','body','image']
