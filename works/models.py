from django.db import models
from django.contrib.postgres.fields import ArrayField

class Works(models.Model):
    title = models.CharField(max_length=45)
    iswc = models.CharField(max_length=60, unique=True)
    contributors = ArrayField(models.CharField(max_length=32), blank=True)

    def __str__(self):
        return self.title + ' - ' + str(self.iswc)




