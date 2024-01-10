from django.db import models


class User(models.Model):
    discription = models.TextField(null=True, blank=True)
    email = models.EmailField()
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=128)
