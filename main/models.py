from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models import Q
# Create your models here.

    
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile', default='avatar.png')
    bio = models.TextField()
    
class Post(models.Model):
    image = models.ImageField( upload_to='posts',default='avatar.jpg', null=False)
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

    class Meta:
        unique_together = (('user', 'follower'), ) 
    
    def __str__ (self):
        return self.user.username

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

    @classmethod
    def followers_either(cls,user):
        return cls.objects.filter(Q(follower=user.id) | Q(user=user.id))



# Now, in your post method implementation, you would do only this:

# UserFollowing.objects.create(user_id=user.id,
#                              following_user_id=follow.id)
# And then, you can access following and followers easily:

# user = User.objects.get(id=1) # it is just example with id 1
# user.following.all()
# user.followers.all()
class UserMethods:
    def get_suggestions(user):
        # suggestions = (User.objects.exclude(id = user.id))
        # return suggestions
        pass

