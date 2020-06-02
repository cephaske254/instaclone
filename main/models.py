from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
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

    @classmethod
    def search(cls, keywords):
        result = cls.objects.filter(Q(caption__icontains=keywords))
        return result
    
    @classmethod
    def get_by_id(cls,id):
        return cls.objects.filter(id=id).first()


class Like(models.Model):
    pass


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"comment on {self.post.user.username}'s post by {self.post.user.username}"

    @classmethod
    def save_comment(cls,user,post,comment):
        comment = cls(user=user, post=post, comment=comment)
        if not cls.objects.filter(user=user.id, post=post.id,comment__icontains=comment).first():
            comment.save()
            return 'Comment posted'
        else :
            return 'Comment already noted'

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