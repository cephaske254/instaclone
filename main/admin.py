from django.contrib import admin
from .models import Comment,Like,Post,Profile, Follower

# Register your models here.
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Profile)
admin.site.register(Follower)
