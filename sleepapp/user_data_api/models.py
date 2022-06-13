from django.db import models

# Create your models here.
class sleepData(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    date = models.DateField()
    hoursSlept= models.IntegerField()
    routine = models.CharField(max_length=20)
    sleepQuality = models.IntegerField()

    