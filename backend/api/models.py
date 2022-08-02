from django.db import models

# Create your models here.
class Intern(models.Model):
    name = models.CharField(max_length=150)
    university = models.CharField(max_length=150)
    course = models.CharField(max_length=150)
    LoB = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    interest1 = models.CharField(max_length=150)
    interest2 = models.CharField(max_length=150)
    interest3 = models.CharField(max_length=150)
    programming1 = models.CharField(max_length=150)
    programming2 = models.CharField(max_length=150)
    request_time = models.FloatField

    def __str__(self):

        return self.name
