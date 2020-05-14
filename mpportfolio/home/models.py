from django.db import models


class Works(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    url=models.URLField(max_length=256)