from django.db import models

# Create your models here.
class Movie(models.Model):
	original_language = models.CharField(max_length=2)
	original_title = models.CharField(max_length=100)
	release_date = models.DateTimeField()
	revenue = models.IntegerField(default=0)
	runtime = models.IntegerField(default=0)
	
	def __str__(self):
		return self.original_title
	
	def is_successful(self):
		return self.revenue >= 150000000
	
	def is_long(self):
		return self.runtime >= 180

class Comment(models.Model):
	username = models.CharField(max_length=50)
	review = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.review