from django.db import models

# Create your models here.

class Family(models.Model):
    full_name = models.CharField(max_length=30)
    DNI = models.IntegerField(unique=True)
    nacimiento = models.CharField(max_length=10)
