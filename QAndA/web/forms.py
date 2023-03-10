from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from api.models import Questions

class QuestionForm(forms.ModelForm):

    class Meta:
        model=Questions
        fields=["title","description","image"]

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

    




