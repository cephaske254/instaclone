from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='media/profiles', null=True, blank=True)

    def __str__(self):
        return self.user.username

    @classmethod
    def save_profile(cls,user,bio,image):
        user_info_old = cls.objects.filter(user=user).first()
        print (user_info_old)
        if user_info_old is not None:
            user_info_old.bio=bio
            if image is not None:
                user_info_old.profile_image=image
            user_info_old.save()
        else:
            user_info = cls(user=user, bio=bio,profile_image=image)
            user_info.save()

    def save_details(user, first_name,last_name, email):
        user = User.objects.filter(username=user.username).first()
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        

