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

class Monitoramento(models.Model):
    piscina = models.ForeignKey(Piscina, on_delete=models.CASCADE)
    ph = models.DecimalField(max_digits=4, decimal_places=2)
    temperatura = models.DecimalField(max_digits=5, decimal_places=2)
    data_medicao = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"{self.piscina.nome} - {self.data_medicao}"


