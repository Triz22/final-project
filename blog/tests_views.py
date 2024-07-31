from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post,Comment,News
from blog.forms import PostForm, CommentForm


# Create your tests here.

class BlogViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpword',)
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        self.news = News.object.create(title='Test News', content='Test Content')