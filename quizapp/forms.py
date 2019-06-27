from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import QuizUser,Qualification,Experience,Quiz,QuizAnswer

class QuizUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = QuizUser
        fields = ('username','first_name','password1','password2', 'email','nationality','phone','researchInterest','disiplines','researchMethod','referenceStyle','profile','street1','street2','state','city','postcode','country')

class QualificationForm(ModelForm):
    class Meta:
        model = Qualification
        exclude = ['userid']

class ExperienceForm(ModelForm):
    class Meta :
        model = Experience
        exclude = ['userid']
class QuizForm(ModelForm):
    class Meta:
        model = QuizAnswer
        fields = ['inputopt','question']

