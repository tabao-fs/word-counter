from django.db import models


class Website(models.Model):
    """
    Website
    """
    word = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    count = models.IntegerField()
