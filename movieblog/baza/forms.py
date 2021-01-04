from django import forms
import datetime

class CommentForm(forms.Form):
	review = forms.CharField(max_length=2000)
	rating = forms.CharField(widget=forms.Select(choices=[('like', 'like'), ('dislike', 'dislike')]), required=False)

class MovieForm(forms.Form):
	original_language = forms.CharField(max_length=2)
	original_title = forms.CharField(max_length=100)
	release_date = forms.DateTimeField(initial=datetime.date.today)
	revenue = forms.IntegerField()
	runtime = forms.IntegerField()