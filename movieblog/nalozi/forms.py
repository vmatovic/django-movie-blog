from django import forms

class RegisterForm(forms.Form):
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=60)
	username = forms.CharField(max_length=50)
	password = forms.CharField(max_length=40, widget=forms.PasswordInput)
	
class LoginForm(forms.Form):
	username = forms.CharField(max_length=50)
	password = forms.CharField(max_length=40, widget=forms.PasswordInput)