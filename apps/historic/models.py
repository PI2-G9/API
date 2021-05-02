from django.db import models
from django.contrib.auth.models import User
from django import forms
from apps.accounts.models import UserProfile


class Historic(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    data_hr_entrada = models.DateTimeField(auto_now_add=True)
    data_hr_saida = models.DateTimeField(auto_now_add=True)
    temperatura = models.CharField(max_length=2)

    def __str__(self):
        return self.login_pessoa
