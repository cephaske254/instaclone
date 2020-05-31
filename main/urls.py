from django.urls import path
from . import views


urlpatterns =[
    path('',views.home,name='home'),
    path('<username>/',views.profile,name='profile'),
    path('follow/<username>',views.follow,name='follow'),
]