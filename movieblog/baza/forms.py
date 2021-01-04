from django import forms

class CommentForm(forms.Form):
	review = forms.CharField(max_length=2000)
	rating = forms.CharField(widget=forms.Select(choices=[('like', 'like'), ('dislike', 'dislike')]), required=False)