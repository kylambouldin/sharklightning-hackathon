from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required(login_url='auth/login/')
def home(request):
    return render(request, 'simpler/home.html')

def login(request):
    return render(request, 'login.html')

def loggedin(request):
    user = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=user, password=password)
    if user is not None:
      return render(request,'simpler/home.html')
      #if user.is_active:
      #  print("User is valid, active and authenticated")
      #else:
      #  print("The password is valid, but the account has been disabled!")
    else:
      return render(request,'login.html')
      # the authentication system was unable to verify the username and password
      #print("The username and password were incorrect.")

def logout_view(request):
    logout(request)
    return render(request,'login.html')
