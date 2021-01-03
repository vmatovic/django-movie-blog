from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from baza.models import Comment

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = request.POST
		username = form.get('username', '')
		password = form.get('password', '')
		first_name = form.get('first_name', '')
		last_name = form.get('last_name', '')
		user = User.objects.create_user(username=username, password=password,
			first_name=first_name, last_name=last_name)
		
		user = authenticate(request, username=username, password=password)
		if user is not None:
			django_login(request, user)
			return redirect('baza:home')
		else:
			return HttpResponse('registration error')
	
	return render(request, 'register.html')

def login(request):
	if request.user.is_authenticated:
		return redirect('baza:home')
	
	if request.method == 'POST':
		form = request.POST
		username = form.get('username', '')
		password = form.get('password', '')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			django_login(request, user)
			return redirect('baza:home')
		else:
			return HttpResponse('login error')
	
	return render(request, 'login.html')

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