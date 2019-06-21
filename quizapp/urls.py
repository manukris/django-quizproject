from django.urls import path
from . import views

urlpatterns = [

    path('', views.ViewTemplate.as_view(),name="reg2"),
]