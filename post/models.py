from django.db import models
from django.contrib.auth.models import User
from topics.models import Topics
from community.models import Community


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    topic = models.ManyToManyField(Topics, through='Post_Topic')


class Post_Topic(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
