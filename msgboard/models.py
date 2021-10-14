# from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone


class Message(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
