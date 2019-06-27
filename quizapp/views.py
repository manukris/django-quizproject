from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import QuizUser,Qualification,Quiz,QuizAnswer
from .forms import QuizUserCreationForm,QualificationForm,ExperienceForm,QuizForm

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


class QuizView(ListView):
    template_name = "quizapp/quiz.html"
    model         = Quiz
    paginate_by   = 1


    def get_context_data(self, *, object_list=None, **kwargs):
        contextData = super().get_context_data( object_list=None, **kwargs)
        contextData['form'] = QuizForm()
        return contextData


def quizFormSubmit(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quizanswer = form.save(commit=False)


            if quizanswer.question.answer == quizanswer.inputopt:
                status = 1
            else:
                status = 2
            quizanswer.userid = QuizUser.objects.get(pk=2)
            quizanswer.status = status
            quizanswer.save()
            return HttpResponse("submit")

        else:
            return HttpResponse(form.errors)



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






