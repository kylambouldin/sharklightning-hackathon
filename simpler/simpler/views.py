from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

@login_required(login_url='auth/login/')
def home(request):
    return render(request, 'simpler/home.html')

def loginpage(request):
    return render(request, 'login.html')

def loggedin(request):
    user = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=user, password=password)
    if user is not None:
      login(request,user)
      return render(request,'simpler/home.html')
    else:
      return render(request,'login.html')

def logout_view(request):
    logout(request)
    return render(request,'login.html')
