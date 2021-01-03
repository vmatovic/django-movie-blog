from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.http import HttpResponse

# Create your views here.
def register(request):
	if request.user.is_authenticated:
		return HttpResponse(request.user.username)
		#return redirect('baza:home')
	
	
	return render(request, 'register.html')

def login(request):
	return HttpResponse('login')

def logout(request):
	if request.user.is_authenticated:
		django_logout(request)
		return redirect('baza:home')
	
	return HttpResponse('logout')