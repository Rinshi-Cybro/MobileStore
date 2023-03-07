from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,FormView,View
from django.contrib.auth.models import User
from .forms import UserRegForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.
class Home(TemplateView):
    template_name='home.html'
    

class UserRegView(CreateView):
    template_name='reg.html'
    model=User
    form_class=UserRegForm
    success_url=reverse_lazy('home')


class LoginView(FormView):
    form_class=LoginForm
    template_name='login.html'
    def post(self,request):
        uname=request.POST.get('username')
        pswd=request.POST.get('password')
        user=authenticate(request,username=uname,password=pswd)
        if user:
            if user.usertype=="store":
                login(request,user)
                return redirect('shome')
            else:
                login(request,user)
                return redirect('uhome')
        else:
            messages.error(request,"Login Failed!!!")
            return redirect('log') 

class SingOut(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('log')


               
 

