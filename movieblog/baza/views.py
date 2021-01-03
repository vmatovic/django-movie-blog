from django.shortcuts import render
from baza.models import Movie, Comment

# Create your views here.
def home_page(request):
	popular_movies = Movie.objects.filter(revenue__gte=650000000)
	return render(request, 'home.html', {'movies': popular_movies})