from Workshop.settings import DEFAULT_AUTO_FIELD
from django.db import models
from datetime import datetime
# Create your models here.

class Situation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
       return super().__str__()

class UserMessage(models.Model):
    firstName = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    age = models.IntegerField()
    description = models.CharField(max_length=1000)
    bullyDate = models.DateField()
    createAt = models.DateTimeField(default=datetime.now)
    anonym = models.BooleanField(default=False)
    isYou = models.BooleanField(default=True)
    situation = models.ForeignKey(Situation, on_delete=models.CASCADE)
    status = models.NullBooleanField()
    
    def __str__(self) -> str:
       return super().__str__()
