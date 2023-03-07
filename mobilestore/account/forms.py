from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class UserRegForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'first_name','last_name','email','username','password1','password2','phone','address','usertype',           
        ]

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter the username","class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Enter the Password","class":"form-control"}))
    