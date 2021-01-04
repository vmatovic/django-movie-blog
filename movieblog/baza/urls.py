from django.urls import path
from . import views

app_name = "baza"

urlpatterns = [
	path('', views.home_page, name='home'),
	path('movie/<int:id>', views.movie_page, name='movie_page'),
	path('movie/search/', views.movie_page_by_name, name='movie_page_by_name'),
	path('comment/<int:id>', views.post_comment, name='post_comment'),
	path('deletecomment/<int:id>', views.delete_comment, name='delete_comment'),
	path('changecomment/<int:id>', views.change_comment, name='change_comment'),
	path('addfilm/', views.add_movie, name='add_movie')
]