from django.db import models
from django.contrib.auth.models import User




class Post(models.Model):
    image = models.ImageField(upload_to='posts')
    caption = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.caption

    @classmethod
    def get_posts(cls):
        return cls.objects.all()


class Like(models.Model):
    pass


class Comment(models.Model):
    pass


class Follower(models.Model):
    pass

class UserMethods:
    def get_suggestions(self):
        return None