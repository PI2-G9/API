from django.db import models

from apps.profiles.models import Profile


class Event(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    entrance = models.BooleanField("Entrou?", null=False)
    temp = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.user.nome} {'entrou' if self.entrance else 'saiu'} às {self.timestamp}"
