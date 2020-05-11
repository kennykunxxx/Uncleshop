from django.db import models

# Create your models here.

class Message(models.Model):
    message = models.CharField(max_length=250)
    date_now = models.DateTimeField(auto_now_add=True)