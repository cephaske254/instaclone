from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models import Q
from random import shuffle
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

    @classmethod
    def get_posts(cls):
        return cls.objects.all()

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
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers') #my id when i follow
    
    @classmethod
    def follow_unfollow(cls, username, myusername):
        user = User.objects.filter(username=username).first() #the person
        me = User.objects.filter(username=myusername).first() #me/ follower col
        
        try:
            cls.objects.get(user=user, follower=me).delete()
            return 'Unfollowed'
        except:
            cls.objects.create(user=user, follower=me)
            return 'Followed'
    def __str__ (self):
        return self.user.username
    
class ProfileImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ImageField(upload_to='profile')


# Now, in your post method implementation, you would do only this:

# UserFollowing.objects.create(user_id=user.id,
#                              following_user_id=follow.id)
# And then, you can access following and followers easily:

# user = User.objects.get(id=1) # it is just example with id 1
# user.following.all()
# user.followers.all()
class UserMethods(User):
    def get_suggestions():
        suggestions = User.objects.order_by("?")[:10]
        return suggestions