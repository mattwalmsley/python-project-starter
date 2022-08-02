from django.db import models

# Create your models here.
class AnalyseMatches(models.Model):
    name = models.CharField(max_length=150)
    preference1 = models.CharField(max_length=150)
    preference2 = models.CharField(max_length=150)
    preference3 = models.CharField(max_length=150)

    def __str__(self):

        return self.name
