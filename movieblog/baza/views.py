from django.shortcuts import render, get_object_or_404, redirect
from baza.models import Movie, Comment
from datetime import date
from django.http import HttpResponse
from .forms import *
from django.forms.models import model_to_dict

# Create your views here.
def home_page(request):
	popular_movies = Movie.objects.filter(revenue__gte=650000000)
	return render(request, 'home.html', {'movies': popular_movies})

def movie_page(request, id):
	mov = get_object_or_404(Movie, pk=id)
	comments = Comment.objects.filter(movie=id)
	form = CommentForm()
	return render(request, 'movie_page.html', {'movie': mov, 'comments': comments, 'form': form})

def movie_page_by_name(request):
	mov_title = request.POST.get('query', '')
	mov_title = mov_title.title()
	mov = get_object_or_404(Movie, original_title=mov_title)
	comments = Comment.objects.filter(movie=mov)
	form = CommentForm()
	return render(request, 'movie_page.html', {'movie': mov, 'comments': comments, 'form': form})

def post_comment(request, id):
	mov = get_object_or_404(Movie, pk=id)
	comments = Comment.objects.filter(movie=id)
	if request.method == 'POST':
		form = CommentForm(request.POST or None)
		if form.is_valid():
			review = request.POST.get('review', '')
			rating = request.POST.get('rating', '')
			if rating == 'like':
				mov.likes += 1
			else:
				mov.dislikes += 1
			mov.save()
			comment = Comment(username=request.user.username, review=review, date=date.today(), movie=mov)
			comment.save()
		else:
			HttpResponse('comment error')
	
	return redirect('baza:movie_page', id=id)
	
def delete_comment(request, id):
	if request.user.is_authenticated:
		comment = Comment.objects.get(id=id)
		comment.delete()
		return redirect('nalozi:userpage')

def change_comment(request, id):
	form = CommentForm()
	comment = Comment.objects.get(id=id)
	if request.user.is_authenticated:
		
		if request.method == 'POST':
			form = CommentForm(request.POST or None)
			if form.is_valid():
				form = request.POST
				new_review = form.get('review', '')
				comment.review = new_review
				comment.save()
				return redirect('nalozi:userpage')
			else:
				return HttpResponse('comment error')
	
	return render(request, 'change_comment.html', {'form': form, 'comment': comment})

def add_movie(request):
	if request.user.is_authenticated:
		form = MovieForm()
		if request.method == 'POST':
			form = MovieForm(request.POST or None)
			if form.is_valid():
				form = request.POST
				or_title = form.get('original_title', '')
				or_lang = form.get('original_language', '')
				date = form.get('release_date', '')
				revenue = form.get('revenue', '')
				runtime = form.get('runtime', '')
				mov = Movie(original_language=or_lang, original_title=or_title, release_date=date,
					revenue=revenue, runtime=runtime)
				mov.save()
				return redirect('nalozi:userpage')
		return render(request, 'add_movie.html', {'form': form})
	else:
		HttpResponse('movie adding error')

def change_movie(request, id):
	if request.user.is_authenticated:
		mov = get_object_or_404(Movie, pk=id)
		form = MovieForm(initial=model_to_dict(mov))
		if request.method == 'POST':
			form = MovieForm(request.POST or None)
			if form.is_valid():
				form = request.POST
				mov.original_title = form.get('original_title', '')
				mov.original_language = form.get('original_language', '')
				mov.release_date = form.get('release_date', '')
				mov.revenue = form.get('revenue', '')
				mov.runtime = form.get('runtime', '')
				mov.save()
				return redirect('baza:home')
		return render(request, 'change_movie.html', {'form': form, 'mid': id})
	else:
		HttpResponse('movie changing error')