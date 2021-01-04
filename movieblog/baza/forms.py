from django import forms

class CommentForm(forms.Form):
	review = forms.CharField(max_length=2000)