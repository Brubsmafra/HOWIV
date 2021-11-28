from django.db import models

class Assist(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    endereco = models.CharField(max_length=50)

