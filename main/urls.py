from django.urls import path
from . import views


urlpatterns =[
    path('',views.home,name='home'),
    path('follow/<username>',views.follow,name='follow'),
]