from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserPost(models.Model):
    
    user = models.ForeignKey(User, related_name="post", on_delete=models.CASCADE)
    title = models.TextField(max_length=5000, default='Code Query')
    code = models.TextField(max_length=5000)
    language = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.DO_NOTHING)
    user_post = models.ForeignKey(UserPost, related_name="user_post", on_delete=models.CASCADE)
    content = models.TextField(max_length=5000)
    
    def __str__(self):
        return f"{self.user_post.user.username}'s response: {self.user_post.title}" 
    