from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import QuizUser

class QuizUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = QuizUser
        fields = ('username', 'email')