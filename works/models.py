from django.db import models

class Works(models.Model):
    title = models.CharField(max_length=45)
    iswc = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.title + ' - ' + self.iswc


class Contributor(models.Model):
    name = models.CharField(max_length=35)
    works = models.ManyToManyField(Works)

    def __str__(self):
        return self.name

