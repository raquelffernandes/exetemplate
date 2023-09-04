from django.db import models
from datetime import datetime

# Create your models here.
class Amani(models.Model):
    nome_card = models.CharField(max_length=200)
    description = models.TextField()
    precoAtual = models.DecimalField(default= 000, max_digits= 5, decimal_places=00)
    Desconto = models.DecimalField(default= 000, max_digits= 5, decimal_places=00)
    path = models.ImageField(upload_to="images/")
    date_create = models.DateTimeField(default=datetime.now, blank =True)

class Carrossel(models.Model):
    name_card = models.CharField(max_length=200)
    description = models.TextField()
    path = models.ImageField(upload_to="images/")
    date_create = models.DateTimeField(default=datetime.now, blank= True)

class Imagens(models.Model):
    name_card = models.CharField(max_length=200)   
    path = models.ImageField(upload_to="images/")
    date_create = models.DateTimeField(default=datetime.now, blank= True) 