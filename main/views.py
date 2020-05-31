from django.shortcuts import render, HttpResponse, Http404
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
        raise Http404
    else:
        user = User.objects.filter(username=username).first()
    return render(request, 'profile.html',
                  {
                      'title':f'Profile | @{username}',
                      'user':user,
                  })

def follow(request, username):
    user = User.objects.filter(username=username).first()
    following = user.following.all()
    followers = user.followers.all()
    follow_unfollow = Follower.follow_unfollow(username,request.user)
    return HttpResponse(follow_unfollow)



