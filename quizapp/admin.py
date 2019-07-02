from django.contrib import admin

# Register your models here.

from .models import QuizUser,Qualification,Experience,Quiz,QuizAnswer,QualifyDegree



admin.site.register(QuizUser)

admin.site.register(Qualification)



admin.site.register(Experience)

admin.site.register(Quiz)
admin.site.register(QuizAnswer)
admin.site.register(QualifyDegree)






