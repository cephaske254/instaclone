from django.shortcuts import render, HttpResponse
from .models import UserMethods, Follower, User, Post
# Create your views here.


def home(request):
    suggestions = UserMethods.get_suggestions()
    posts = Post.get_all()
    return render(request, 'home.html',
                  {
                      'suggestions': suggestions,
                      'posts': posts,
                  })


def profile(request, username=None):
    if not username:
        pass
    else:
        pass
    return render(request, 'profile.html',
                  {

                  })

def follow(request, username):
    user = User.objects.filter(username=username).first()
    following = user.following.all()
    followers = user.followers.all()
    follow_unfollow = Follower.follow_unfollow(username,request.user)
    return HttpResponse(follow_unfollow)



