from django.db import models

# Create your models here.

class Restaurantes(models.Model):
    nome = models.CharField(max_length = 200)
    endereco = models.CharField(max_length = 200)