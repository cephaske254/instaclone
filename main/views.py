from django.shortcuts import render, HttpResponse, Http404, redirect
from .models import Follower, User, Post
from .forms import NewPostForm
from django.contrib.auth.decorators import login_required
from django.forms import ValidationError
# Create your views here.


@login_required()
def home(request):
    if not request.user.profile.first():
        return redirect('update_profile')

    following = request.user.following.all()
    # posts = Post.get_all()
    posts = Post.objects.all()
    return render(request, 'home.html',
                  {
                      'following': following,
                  })


def profile(request, username=None):
    if not request.user.profile.first() and request.user.is_authenticated:
        return redirect('update_profile')

    user = User.objects.filter(username=username).first()
    user_posts = user.posts.all()
    if user is None:
        raise Http404()
    return render(request, 'profile.html',
                  {
                      'title': f'Profile | @{username}',
                      'user': user,
                      'posts': user_posts,
                      'info': user.profile.first(),
                  })


def make_post(request):
    form = NewPostForm()

    if request.method == 'POST' and request.user.is_authenticated:
        form = NewPostForm(request.POST, request.FILES, instance=Post())
        if form.is_valid():
            Post.save_post(request.user, form.cleaned_data.get(
                'caption'), request.FILES['image'])
            return redirect('profile', request.user)

        # return redirect('home')
    return render(request, 'make_post.html',
                  {
                      'form': form,

                  })


def search(request):
    posts = Post.search(request.GET['search'])
    return render(request, 'search.html',
                  {
                      'posts':posts
                  })


def follow(request, username):
    user = User.objects.filter(username=username).first()
    follow_unfollow = Follower.follow_unfollow(username, request.user)
    return HttpResponse(follow_unfollow)
