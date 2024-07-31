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

    def test_share_post_view_get(self):
        
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('share_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/share_post.html')
        self.assertIsInstance(response.context['post_form'], PostForm)

    def test_share_post_view_post_valid(self):

        self.client.login(username='testuser', password='testpassword')
        data = {'title':'New Post', 'content':'New Content'}
        response = self.client.post(reverse('share_post'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title='New Post').exists())
        
    def test_post_detail_view_get(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')
        self.assertContains(response, self.post.title)

