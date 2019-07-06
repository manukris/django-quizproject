from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.




class UserNations(models.Model):
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.country






class QuizUser(AbstractUser):
    nationality      = models.IntegerField(default=0)
    phone            = models.CharField(max_length=50,default="null")
    researchInterest = models.CharField(max_length=60,default="null")
    disiplines       = models.CharField(max_length=70,default="null")
    researchMethod   = models.CharField(max_length=70,default="null")
    referenceStyle   = models.CharField(max_length=200,default="null")
    profile          = models.CharField(max_length=50,default="null")
    street1          = models.CharField(max_length=100, default="null")
    street2          = models.CharField(max_length=100, default="null")
    state            = models.CharField(max_length=100, default="null")
    city             = models.CharField(max_length=100, default="null")
    postcode         = models.CharField(max_length=100, default="null")
    country          = models.ForeignKey(UserNations,on_delete=models.CASCADE,default=1)
    profilepic       = models.ImageField(upload_to='profile',default="profile.jpg")






class QualifyDegree(models.Model):
    degreename = models.CharField(max_length=100)

    def __str__(self):
        return self.degreename



class Qualification(models.Model):
    userid      = models.ForeignKey(QuizUser,on_delete=models.CASCADE)
    university  = models.CharField(max_length=50)
    degreelevel = models.CharField(max_length=50)
    degree      = models.ForeignKey(QualifyDegree,on_delete=models.CASCADE)
    startmonth  = models.CharField(max_length=50)
    endmonth    = models.CharField(max_length=50)
    startyear   = models.CharField(max_length=50)
    endyear     = models.CharField(max_length=50)
    document    = models.FileField(upload_to='documents/')
    icons       = models.ImageField(upload_to='qualification/',default='qualification/harvard.png')

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
    icons = models.ImageField(upload_to='experience/',default='experience/british-airways.png')



class Quote(models.Model):
    userid = models.ForeignKey(QuizUser,on_delete=models.CASCADE)
    title  = models.CharField(max_length=100)
    displines  = models.CharField(max_length=100)
    price  = models.IntegerField(max_length=100)
    description  = models.TextField()
    firstname  = models.CharField(max_length=100)
    lastname  = models.CharField(max_length=100)
    email  = models.CharField(max_length=100)
    wordcount  = models.CharField(max_length=100)
    document = models.FileField(upload_to="quotes/")


class Papper(models.Model):
    userid = models.ForeignKey(QuizUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    displines = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    description = models.TextField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    wordcount = models.CharField(max_length=100)
    deadline = models.CharField(max_length=100)
    document = models.FileField(upload_to="pappers/")



class Quiz(models.Model):
    question = models.TextField()
    option1  = models.CharField(max_length=200)
    option2  = models.CharField(max_length=200)
    option3  = models.CharField(max_length=200)
    option4  = models.CharField(max_length=200)
    answer   = models.IntegerField()

class QuizAnswer(models.Model):
    userid   = models.ForeignKey(QuizUser,on_delete=models.CASCADE)
    question = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    inputopt   = models.IntegerField()
    status   = models.IntegerField(default=0)






