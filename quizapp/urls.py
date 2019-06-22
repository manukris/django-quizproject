from django.urls import path
from . import views

urlpatterns = [

    path('', views.ViewTemplate.as_view(),name="reg2"),
    path('add/', views.Adduser.as_view(), name="reg2"),
    path('quiz/', views.QuizView.as_view(), name="quiz"),
]