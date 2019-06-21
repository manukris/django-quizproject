from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.





class ViewTemplate(TemplateView):
    template_name = "quizapp/registration2.html"