from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('search/',views.search,name='search'),
    path('view_post/<post_id>',views.view_post,name='view_post'),
    path('make_post/',views.make_post,name='make_post'),
    path('<username>/',views.profile,name='profile'),
    path('follow/<username>',views.follow,name='follow'),
    path('like/<post_id>',views.like,name='like'),
]