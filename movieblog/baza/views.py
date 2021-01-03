from django.shortcuts import render, get_object_or_404, redirect
from baza.models import Movie, Comment
from datetime import date

# Create your views here.
def home_page(request):
	popular_movies = Movie.objects.filter(revenue__gte=650000000)
	return render(request, 'home.html', {'movies': popular_movies})

def movie_page(request, id):
	mov = get_object_or_404(Movie, pk=id)
	comments = Comment.objects.filter(movie=id)
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