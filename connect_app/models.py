from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    owner = models.ForeignKey('auth.User', related_name='connect_app', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        to=Post, on_delete=models.CASCADE, related_name='comments')
    commented_by = models.CharField(max_length=150)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.commented_by)
