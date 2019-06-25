from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class QuizUser(AbstractUser):
    nationality = models.CharField(max_length=50,default="null")
    phone       = models.CharField(max_length=50,default="null")
    researchInterest = models.CharField(max_length=60,default="null")
    disiplines = models.CharField(max_length=70,default="null")
    researchMethod = models.CharField(max_length=200,default="null")
    referenceStyle = models.CharField(max_length=200,default="null")
    profile        = models.CharField(max_length=50,default="null")
    street1 = models.CharField(max_length=100, default="null")
    street2 = models.CharField(max_length=100, default="null")
    state = models.CharField(max_length=100, default="null")
    city = models.CharField(max_length=100, default="null")
    postcode = models.CharField(max_length=100, default="null")
    country = models.CharField(max_length=100, default="null")




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

class Experience(models.Model):
    userid = models.ForeignKey(QuizUser, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    startmonth = models.CharField(max_length=50)
    endmonth = models.CharField(max_length=50)
    startyear = models.CharField(max_length=50)
    endyear = models.CharField(max_length=50)
    iscurrent = models.BooleanField(default=False)




