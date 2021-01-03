from django.shortcuts import render, get_object_or_404, redirect
from baza.models import Movie, Comment
from datetime import date
from django.http import HttpResponse

# Create your views here.
def home_page(request):
	popular_movies = Movie.objects.filter(revenue__gte=650000000)
	return render(request, 'home.html', {'movies': popular_movies})

def movie_page(request, id):
	mov = get_object_or_404(Movie, pk=id)
	comments = Comment.objects.filter(movie=id)
	return render(request, 'movie_page.html', {'movie': mov, 'comments': comments})

def movie_page_by_name(request):
	mov_title = request.POST.get('query', '')
	mov_title = mov_title.title()
	mov = get_object_or_404(Movie, original_title=mov_title)
	comments = Comment.objects.filter(movie=mov)
	return render(request, 'movie_page.html', {'movie': mov, 'comments': comments})

def post_comment(request, id):
	mov = get_object_or_404(Movie, pk=id)
	comments = Comment.objects.filter(movie=id)
	if request.method == 'POST':
		form = request.POST
		comment_text = form.get('comment', '')
		comment = Comment(username=request.user.username, review=comment_text, date=date.today(), movie=mov)
		comment.save()
	return redirect('baza:movie_page', id=id)
	
def delete_comment(request, id):
	if request.user.is_authenticated:
		comment = Comment.objects.get(id=id)
		comment.delete()
		return redirect('nalozi:userpage')

def change_comment(request, id):
	return HttpResponse('change comment')