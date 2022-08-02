from django.db import models

# Create your models here.
class AnalyseMatches(models.Model):
    name = models.CharField(max_length=150)
    preference1 = models.CharField(max_length=150)
    preference2 = models.CharField(max_length=150)
    preference3 = models.CharField(max_length=150)

    def __str__(self):

        return self.name

class ResultModel(models.Model):
    internName = models.CharField(max_length=150)
    buddy1 = models.CharField(max_length=150)
    buddy2 = models.CharField(max_length=150)
    buddy3 = models.CharField(max_length=150)

    def __str__(self):

        return self.name
