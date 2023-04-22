from django.shortcuts import render, redirect
from django.contrib.auth import logout
def login(request):
    return render(request, 'user/login.html')
    
def logout_view(request):
    logout(request)
    return redirect('/')

