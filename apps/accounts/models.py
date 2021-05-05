from django.db import models
from phone_field import PhoneField
from cpf_field.models import CPFField
from django.contrib.auth.models import User
from composite_field import CompositeField


class EnderecoField(CompositeField):
    cep = models.CharField(max_length=8)
    nome_rua = models.CharField(max_length=30)
    numero = models.CharField(max_length=3)
    nome_cidade = models.CharField(max_length=30)
    estado = models.CharField('UF', max_length=2)
    #
    # def __str__(self):
    #     return f'{self.nome_cidade} - {self.estado}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    cpf = CPFField('CPF', primary_key=True)
    nome = models.CharField('Nome Completo', max_length=90)
    data_nascimento = models.DateField('Data de Nascimento')
    telefone = PhoneField(blank=True, help_text='Telefone para contato')
    endereco = EnderecoField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_employee = models.BooleanField('Funcionário', default=False)
    is_admin = models.BooleanField('Administrador', default=False)

    def __str__(self):
        return self.nome


class PhotoUser(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="photos")
    photo1 = models.ImageField(upload_to='photo')
    photo2 = models.ImageField(upload_to='photo')
    photo3 = models.ImageField(upload_to='photo')

    def __str__(self):
        return [self.photo1, self.photo2, self.photo3]


class HistoricUser(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    entrance = models.BooleanField("Entrou?", null=False)
    temp = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.user.nome} {'entrou' if self.entrance else 'saiu'} às {self.hora}"
