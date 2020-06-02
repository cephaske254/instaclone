from django.shortcuts import render, HttpResponse, Http404, redirect
from .models import Follower, User, Post, Comment
from .forms import NewPostForm
from django.contrib.auth.decorators import login_required
from django.forms import ValidationError
from django.db.models import Q
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
    try:
        user_posts = user.posts.all()
    except:
        user_posts = None

    if user is None:
        raise Http404()
    return render(request, 'profile.html',
                  {
                      'title': f'Profile | @{username}',
                      'user': user,
                      'posts': user_posts,
                      'info': user.profile.first(),
                  })


@login_required()
def view_post(request, post_id):
    post = Post.get_by_id(post_id)
    comment_feedback=''
    if request.method =="POST":
        comment= request.POST['comment']
        print(comment)
        comment_feedback=Comment.save_comment(request.user,post,comment)
    return render(request, 'single_post.html',
                  {
                      'post': post,
                      'comment_feedback':comment_feedback
                  })


@login_required()
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

@login_required()
def search(request):
    if not request.GET.get('search'):
        return redirect('home')
    posts = Post.search(request.GET['search'])
    users = User.objects.filter(Q(username__icontains=request.GET['search']), Q(email__icontains=request.GET['search']))
    return render(request, 'search.html',
                  {
                      'posts': posts,
                      'users':users
                  })


@login_required()
def follow(request, username):
    user = User.objects.filter(username=username).first()
    follow_unfollow = Follower.follow_unfollow(username, request.user)
    if request.META['HTTP_REFERER']:
        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect('profile', username)