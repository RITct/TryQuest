from django.contrib.auth.models import User
from django.db import models


class Admin(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField()


class AdminGroup(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(Admin)
