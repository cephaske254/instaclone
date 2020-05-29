from django.urls import path, include
from . import views
# from django_registration.backends.one_step
# from django_registration.backends.one_step.urls import 
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns =[
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='django_registration/login_form.html',redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]