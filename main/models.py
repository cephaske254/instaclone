from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
# Create your models here.

class Post(models.Model):
    image = models.ImageField( upload_to='posts',default='avatar.jpg')
    caption = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.caption

    @classmethod
    def get_single(cls, id):
        return cls.objects(id=1)
        
    def save_image(self):
        self.save()
    
    @classmethod
    def get_all(cls):
        return cls.objects.all()
    
    @classmethod
    def search(cls, search):
        results = cls.objects.filter(Q(user_username__icontains=search) | Q(caption__icontains=search))
        return results

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following') #his id
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers') #my id
