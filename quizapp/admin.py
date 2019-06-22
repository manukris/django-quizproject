from django.contrib import admin

# Register your models here.

from .models import QuizUser,Qualification



admin.site.register(QuizUser)

admin.site.register(Qualification)
