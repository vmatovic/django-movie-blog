from django.shortcuts import render, get_object_or_404
from baza.models import Movie, Comment

# Create your views here.
def home_page(request):
	popular_movies = Movie.objects.filter(revenue__gte=650000000)
	return render(request, 'home.html', {'movies': popular_movies})

def movie_page(request, id):
	mov = get_object_or_404(Movie, pk=id)
	return render(request, 'movie_page.html', {'movie': mov})