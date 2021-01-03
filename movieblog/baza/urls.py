from django.urls import path
from . import views

app_name = "baza"

urlpatterns = [
	path('', views.home_page, name='home'),
	path('movie/<int:id>', views.movie_page, name='movie_page')
]