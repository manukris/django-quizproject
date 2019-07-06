from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import QuizUser,Qualification,Experience,Quiz,QuizAnswer

class QuizUserCreationForm(UserCreationForm):

    rmethods = (
                ("1", "Quantitative"),
                ("2", "Qualitative"),
                ("3", "Others"),
               )
    rstyle = (
               ("1","Harvard"),
               ("2","Oxford"),
               ("3","Chicago"),
               ("4","APA"),
               ("5","MLA"),
               ("6","Others"),
             )
    researchMethod = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=rmethods)
    referenceStyle = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=rstyle)


    class Meta(UserCreationForm):
        model = QuizUser
        fields = ('username','first_name','password1','password2', 'email','phone','researchInterest','disiplines','street1','street2','state','city','postcode','country','nationality','profilepic')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country'].widget.attrs.update({
            'id': 'country',
            'class': 'form-control light-input select',
            })


class QualificationForm(ModelForm):
    class Meta:
        model   = Qualification
        exclude = ['userid']

class ExperienceForm(ModelForm):
    class Meta :
        model = Experience
        exclude = ['userid']
class QuizForm(ModelForm):
    class Meta:
        model  = QuizAnswer
        fields = ['inputopt','question']

class ExpImageForm(ModelForm):
    expid = forms.CharField(max_length=20)
    class Meta:
        model = Experience
        fields = ['icons']

class QualifyImageForm(ModelForm):
    expid = forms.CharField(max_length=20)
    class Meta:
        model = Qualification
        fields = ['icons']

