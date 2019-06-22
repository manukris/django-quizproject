from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class QuizUser(AbstractUser):
    nationality = models.CharField(max_length=50)
    phone       = models.CharField(max_length=50)
    researchInterest = models.CharField(max_length=60)
    disiplines = models.CharField(max_length=70)




