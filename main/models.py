from django.db import models
from django.contrib.auth.models import User
import datetime

class Post(models.Model):
    image = models.ImageField(upload_to='posts')
    caption = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    date = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.caption

    @classmethod
    def get_posts(cls):
        return cls.objects.all()

    @classmethod
    def save_post(cls,user, caption, image):
        post = cls(user=user,caption=caption, image=image)
        print(image)
        post.save()


class Like(models.Model):
    pass


class Comment(models.Model):
    pass


class Follower(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='followers')
    followed_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.followed_by.username} following {self.user.username}'

    @classmethod
    def follow_unfollow(cls, user, followed_by):
        user_details = User.objects.filter(username=user).first()
        follower = cls(user=user_details,followed_by=followed_by)
        if not user == followed_by.username:
            try:
                cls.objects.filter(user=user_details.id).first().delete()
                return 'unfollowed'
            except:
                follower.save()
                return 'followed'
        return 'Cannot follow yourself'