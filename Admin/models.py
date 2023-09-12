from django.db import models

# Create your models here.
class District(models.Model):
    name=models.CharField(max_length=50)
class Catgeory(models.Model):
    category=models.CharField(max_length=50)