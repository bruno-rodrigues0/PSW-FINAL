from django.db import models
from django.contrib.auth.models import User
from post.models import Post


class Comment(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
