from django.db import models

# Create your models here.
class servise(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state =models.CharField(max_length=30)
    servise_type = models.CharField(max_length=64)
    price = models.IntegerField()       

