from django.db import models
from django.contrib.auth.models import User

class Topics (models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
