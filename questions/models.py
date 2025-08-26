from django.db import models
from django.contrib.auth.models import User
from topics.models import Topics

class Questions(models.Model):
    statement = models.CharField(max_length=1000)
    alternative_a = models.BooleanField()
    alternative_b = models.BooleanField()
    alternative_c = models.BooleanField()
    alternative_d = models.BooleanField()
    alternative_e = models.BooleanField()
    topic = models.ManyToManyField(Topics, through='Question_Topic')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Question_Topic(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    