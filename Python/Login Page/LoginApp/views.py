
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def index(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
  
    user = authenticate(username = username, password = password)
    if user:
        login(request, user)
        return render (request, 'home.html')

    return render (request, 'index.html',{'user':user})

def Home(request):

    return render(request, "home.html")

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'index.html')