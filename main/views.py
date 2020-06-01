from django.shortcuts import render, HttpResponse, Http404, redirect
from .models import UserMethods, Follower, User, Post
from .forms import NewPostForm
from django.contrib.auth.decorators import login_required 
from django.forms import ValidationError
# Create your views here.

@login_required()
def home(request):
    suggestions = UserMethods.get_suggestions(request.user)
    # posts = Post.get_all()
    posts = Post.objects.all()
    return render(request, 'home.html',
                  {
                      'suggestions': suggestions,
                      'posts': posts,
                  })


def profile(request, username=None):
    form = NewPostForm()
    user = User.objects.filter(username=username).first()
    user_posts = Post.objects.filter(user =request.user.id)
    if user is None:
       raise Http404()

    if request.method == 'POST' and request.user.is_authenticated:
        form = NewPostForm(request.POST,request.FILES)
        if len(request.FILES) <= 0:
            form.add_error('image',ValidationError('Image file is required'))
        else:
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    return render(request, 'profile.html',
                  {
                      'title':f'Profile | @{username}',
                      'user':user,
                      'form':form,
                      'posts':user_posts,
                      'info':user.profile.first(),
                  })


def follow(request, username):
    user = User.objects.filter(username=username).first()
    following = user.following.all()
    followers = user.followers.all()
    follow_unfollow = Follower.follow_unfollow(username,request.user)
    return HttpResponse(follow_unfollow)



