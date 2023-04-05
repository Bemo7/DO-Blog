from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime
class CommentForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea,max_length=600)
    

class Search(forms.Form):
    search = forms.CharField(max_length=20)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=40)
    date_of_birth = forms.DateField(initial=datetime.date.today)
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email','date_of_birth', 'password1', 'password2')
        help_texts = {
            'username': None,
            'email': None,
            'password2' : None
        }

class LoginForm(forms.Form):
    username = forms.CharField(min_length=4,max_length=25, required=True)
    password = forms.CharField(widget=forms.PasswordInput)