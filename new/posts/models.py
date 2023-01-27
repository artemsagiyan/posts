from django.db import models
from rest_framework.authtoken.admin import User


# Create your models here.

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    annotation = models.TextField(null=True, blank=True, max_length=500)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)