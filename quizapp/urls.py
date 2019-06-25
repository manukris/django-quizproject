from django.urls import path
from . import views

urlpatterns = [

    path('', views.ViewTemplate.as_view(),name="reg2"),
    path('registration1/', views.AdduserDetails.as_view(), name="reg1"),
    path('registration2/', views.qualificationExpView, name="reg2"),
    path('qualifyadd/', views.addQualification, name="qualifyadd"),
    path('expadd/', views.addExperience, name="expadd"),
    path('quiz/', views.QuizView.as_view(), name="quiz"),
]