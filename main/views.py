from django.shortcuts import render, HttpResponse, Http404
from .models import UserMethods, Follower, User, Post
from .forms import NewPostForm
from django.forms import ValidationError
# Create your views here.


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
    if request.method == 'POST':
        form = NewPostForm(request.POST,request.FILES)
        if len(request.FILES) <= 0:
            form.add_error('image',ValidationError('Image file is required'))
        else:
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            print(form)
    if not username:
        raise Http404
    else:
        user = User.objects.filter(username=username).first()
    return render(request, 'profile.html',
                  {
                      'title':f'Profile | @{username}',
                      'user':user,
                      'form':form,
                  })

def follow(request, username):
    user = User.objects.filter(username=username).first()
    following = user.following.all()
    followers = user.followers.all()
    follow_unfollow = Follower.follow_unfollow(username,request.user)
    return HttpResponse(follow_unfollow)



