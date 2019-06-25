from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import QuizUser,Qualification
from .forms import QuizUserCreationForm,QualificationForm,ExperienceForm

from django.views.decorators.csrf import csrf_exempt


# Create your views here.



class Adduser(CreateView):
    template_name = 'quizapp/adduser.html'
    form_class = QuizUserCreationForm
    success_url = "/"

class AdduserDetails(CreateView):
    template_name = 'quizapp/registration.html'
    form_class = QuizUserCreationForm
    success_url = reverse_lazy('reg2')

    # def form_valid(self, form):
    #     obj = form.save()
    #     super().form_invalid(form)
    #     return HttpResponse(obj.pk)
    def form_invalid(self, form):
        return HttpResponse(form.errors)



class AddQualification(CreateView):
    template_name = "quizapp/registration2.html"
    model         = Qualification
    fields = ['userid','university','degreelevel','degree','startmonth','endmonth','startyear','endyear','document']


class ViewTemplate(TemplateView):
    template_name = "quizapp/registration2.html"


class QuizView(TemplateView):
    template_name = "quizapp/quiz.html"


def qualificationExpView(request):
    qform = QualificationForm()
    eform = ExperienceForm()
    formdict = dict()
    formdict['qform'] = qform
    formdict['eform'] = eform
    return render(request,'quizapp/registration2.html',formdict)




@csrf_exempt
def addQualification(request):
    if request.method == 'POST':
        form = QualificationForm(request.POST,request.FILES)
        if form.is_valid():
            qualification = form.save(commit=False)
            qualification.userid = QuizUser.objects.get(pk=2)
            qualification.save()

            return HttpResponse("Qualification added")
        else:
            return HttpResponse(form)


@csrf_exempt
def addExperience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.userid = QuizUser.objects.get(pk=2)
            experience.save()
            return HttpResponse("Experience Added")






