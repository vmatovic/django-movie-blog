from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from baza.models import Comment
from .forms import *

# Create your views here.
def register(request):
	form = RegisterForm()
	if request.method == 'POST':
		form = RegisterForm(request.POST or None)
		if form.is_valid():
			username = request.POST.get('username', '')
			password = request.POST.get('password', '')
			first_name = request.POST.get('first_name', '')
			last_name = request.POST.get('last_name', '')
			user = User.objects.create_user(username=username, password=password,
				first_name=first_name, last_name=last_name)
		
			user = authenticate(username=user.username, password=password)
			django_login(request, user)
			return redirect('baza:home')
		else:
			return HttpResponse('registration error')
	
	return render(request, 'register.html', {'form': form})

def login(request):
	if request.user.is_authenticated:
		return redirect('baza:home')
	
	form = LoginForm()
	
	if request.method == 'POST':
		form = LoginForm(request.POST or None)
		if form.is_valid():
			form = request.POST
			username = form.get('username', '')
			password = form.get('password', '')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				django_login(request, user)
				return redirect('baza:home')
			else:
				return HttpResponse('login error')
		else:
			return HttpResponse('login error')
	
	return render(request, 'login.html', {'form': form})

def logout(request):
	if request.user.is_authenticated:
		django_logout(request)
		return redirect('baza:home')
	
	return HttpResponse('logout')

def userpage(request):
	if request.user.is_authenticated:
		reviews = Comment.objects.filter(username=request.user.username)
		return render(request, 'userpage.html', {'user': request.user, 'reviews': reviews})
	else:
		return HttpResponse('user error')