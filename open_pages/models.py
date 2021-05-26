from django.db import models


class Pages(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=200)
    html = models.TextField()

