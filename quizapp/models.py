from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class QuizUser(AbstractUser):
    nationality = models.CharField(max_length=50)
    phone       = models.CharField(max_length=50)
    researchInterest = models.CharField(max_length=60)
    disiplines = models.CharField(max_length=70)

class Qualification(models.Model):
    userid      = models.ForeignKey(QuizUser,on_delete=models.CASCADE)
    university  = models.CharField(max_length=50)
    degreelevel = models.CharField(max_length=50)
    degree      = models.CharField(max_length=50)
    startmonth  = models.CharField(max_length=50)
    endmonth    = models.CharField(max_length=50)
    startyear   = models.CharField(max_length=50)
    endyear     = models.CharField(max_length=50)
    document    = models.FileField(upload_to='documents/')




