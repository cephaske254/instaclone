from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('make_post/',views.make_post,name='make_post'),
    path('<username>/',views.profile,name='profile'),
    path('follow/<username>',views.follow,name='follow'),
]