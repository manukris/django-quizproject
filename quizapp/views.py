from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .models import QuizUser
from .forms import QuizUserCreationForm

# Create your views here.



class Adduser(CreateView):
    template_name = 'quizapp/adduser.html'
    form_class = QuizUserCreationForm
    success_url = "/"



class ViewTemplate(TemplateView):
    template_name = "quizapp/registration2.html"


class QuizView(TemplateView):
    template_name = "quizapp/quiz.html"