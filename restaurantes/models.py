from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Restaurantes(models.Model):
    nome        = models.CharField(max_length = 200)
    endereco    = models.CharField(max_length = 200)
    cnpj        = models.TextField()
    imagem      = models.ImageField(upload_to = 'fotos/%d/%m/%Y/', blank = True)
    descricao   = models.TextField()
    telefone    = models.TextField()
    senha = models.CharField(max_length = 200)