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

    def test_home_page_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

        