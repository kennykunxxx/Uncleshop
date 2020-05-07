from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='home/profile_image', blank=True)