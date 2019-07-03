from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import QuizUser,Qualification,Quiz,QuizAnswer,Experience,UserNations,QualifyDegree
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

    def get_context_data(self, **kwargs):
        contextData = super().get_context_data(object_list=None, **kwargs)
        contextData['nations'] = UserNations.objects.all()
        return contextData

    def form_valid(self, form):

        if form.is_valid():

            user = form.save(commit=False)
            researchMethod = form.cleaned_data['researchMethod']
            referenceStyle = form.cleaned_data['referenceStyle']
            researchMethod = ",".join(researchMethod)
            referenceStyle = ",".join(referenceStyle)
            user.researchMethod = researchMethod
            user.referenceStyle = referenceStyle
            user.save()
            userid = user.pk
            self.request.session['userid'] = userid
            return super().form_valid(form)


    # def form_invalid(self, form):
    #     return HttpResponse(form.errors)



class EditingServiceTemplate(TemplateView):
    template_name = "quizapp/editing_services.html"



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
    ordering = ['?']



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
    formdict['degrees'] = QualifyDegree.objects.all()
    formdict['qform'] = qform
    formdict['eform'] = eform
    return render(request,'quizapp/registration2.html',formdict)



############################################USER PROFILE ##################################################################

class ShowUserProfile(DetailView):
    model         = QuizUser
    template_name = "quizapp/user.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'].nationality = UserNations.objects.get(pk=int(context['object'].nationality))
        context['object'].researchMethod = context['object'].researchMethod.split(',')
        context['object'].referenceStyle = context['object'].referenceStyle.split(',')
        context['qualifications'] = Qualification.objects.filter(userid=self.object.pk)
        context['experience'] = Experience.objects.filter(userid=self.object.pk)
        return context



############################################                  ##################################################################

@csrf_exempt
def addQualification(request):
    if request.method == 'POST':
        form = QualificationForm(request.POST,request.FILES)
        if form.is_valid():
            qualification = form.save(commit=False)
            if 'userid' in request.session:
                userid = request.session['userid']
                qualification.userid = QuizUser.objects.get(pk=userid)
                qualification.save()
            else:
                return HttpResponse("Invalid User")


            return HttpResponse("Qualification added")
        else:
            return HttpResponse(form)


@csrf_exempt
def addExperience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            if 'userid' in request.session:
                userid = request.session['userid']
                experience = form.save(commit=False)
                experience.userid = QuizUser.objects.get(pk=userid)
                experience.save()
            else:
                return HttpResponse("Invalid User")
            return HttpResponse("Experience Added")
