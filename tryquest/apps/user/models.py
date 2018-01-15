from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class QuestUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
