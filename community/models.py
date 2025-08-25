from django.db import models
from django.contrib.auth.models import User


class Community(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='owned_communities')  # dono/criador
    members = models.ManyToManyField(
        User, through='Community_Member', related_name='member_communities')  # participação


class Community_Member(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
