from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User
from django import forms


class Endereco(models.Model):
    cep = models.CharField(max_length=8)
    nome_rua = models.CharField(max_length=30)
    numero = models.CharField(max_length=3)
    nome_cidade = models.CharField(max_length=30)
    estado = models.CharField('UF', max_length=2)

    def __str__(self):
        return f'{self.nome_cidade} - {self.estado}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    cpf = models.CharField('CPF', max_length=11, primary_key=True)
    nome = models.CharField('Nome Completo', max_length=90)
    data_nascimento = models.DateField('Data de Nascimento')
    telefone = PhoneField(blank=True, help_text='Telefone para contato')
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_employee = models.BooleanField('Funcionário', default=False)
    is_admin = models.BooleanField('Administrador', default=False)

    def __str__(self):
        return self.nome
