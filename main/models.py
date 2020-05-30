from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    image = models.ImageField( upload_to='posts',default='avatar.jpg')
    caption = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def save(self):
        self.save()

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
