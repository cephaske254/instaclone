from django.test import TestCase
from .models import Post,Comment,Like

# Create your tests here.

class PostTestClass(TestCase):
    def setUp(self):
        self.new_user = User(username='cephas')
        self.new_user.save()
        self.new_post = Post(user=1,image='default.png',caption='Hello World')
        self.new_post.save()

        
        
