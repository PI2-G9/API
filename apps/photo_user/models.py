from django.db import models
from django.contrib.auth.models import User
from django import forms
from apps.accounts.models import UserProfile


class photo_user(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    photo1 = models.ImageField(upload_to='photo')

    def __str__(self):
        return self.login_pessoa
