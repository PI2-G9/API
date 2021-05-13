from django.db import models
from phone_field import PhoneField
from cpf_field.models import CPFField
from django.contrib.auth.models import User
from composite_field import CompositeField
from django.utils.translation import gettext_lazy as _


class EnderecoField(CompositeField):
    cep = models.CharField(max_length=8)
    nome_rua = models.CharField(max_length=30)
    complemento = models.CharField(max_length=50)
    numero = models.CharField(max_length=5)
    nome_cidade = models.CharField(max_length=30)
    estado = models.CharField('UF', max_length=2)


class Profile(models.Model):
    cpf = CPFField('CPF', primary_key=True)
    nome = models.CharField('Nome Completo', max_length=90)
    data_nascimento = models.DateField('Data de Nascimento')
    telefone = PhoneField(blank=True, help_text='Telefone para contato')
    endereco = EnderecoField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(_("Photo"), upload_to='photos')
    is_employee = models.BooleanField('Funcionário', default=False)
    objects = models.Manager()

    def __str__(self):
        return self.nome
