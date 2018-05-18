from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    subject = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    # tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='topics')
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='topics')

# class Tag(models.Model):
#     label = models.CharField(max_length=20, unique=True)
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='tags')

class Post(models.Model):
    message = models.CharField(max_length=300)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')