from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    TIPOS_USUARIO = [
        ('COMUM', 'Usuário Comum'),
        ('ADMIN', 'Administrador'),
    ]
    
    # Remover username, pois usaremos o email como identificador único
    username = None
    email = models.EmailField('E-mail', unique=True)
    nome_completo = models.CharField('Nome Completo', max_length=100)
    tipo = models.CharField('Tipo', max_length=5, choices=TIPOS_USUARIO, default='COMUM')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome_completo']

    def __str__(self):
        return self.nome_completo


class Piscina(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

