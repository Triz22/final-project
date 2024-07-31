from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post,Comment,News
from blog.forms import PostForm, CommentForm


# Create your tests here.

class BlogViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpword',)
        self.post = Post.objects.create(
        anime_title='Test Anime',
        description='Test Description',
        author=self.user,
        rating=5,
        recommended=True,
        )
        self.client.login(username='testuser', password='testpword')


    def test_home_page_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_share_post_view_get(self):
        
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('share_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/share_post.html')
    

    def test_share_post_view_post_valid(self):

        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('share_post'), {
        'anime_title': 'Another Test Anime',
            'description': 'Test Description for another post',
            'rating': 4,
            'recommended': False,    
        })
        self.assertEqual(response.status_code, 302)
        
        
    def test_post_detail_view_get(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')
        self.assertContains(response, self.post.anime_title)

    def test_post_like_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('post_like', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)
    

    def test_post_detail_view_post_comment(self):
        self.client.login(username='testuser', password='testpassword')
        data = {'body': 'New Comment'}
        response = self.client.post(reverse('post_detail', args=[self.post.id]),{
            'body':'test comment',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Comment submitted, thanks for sharing!')
 
    def test_edit_post_view_get(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('edit_post', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/edit_post.html')

    def test_news_page_view(self):
        response = self.client.get(reverse('news_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/news.html')
    

    def test_delete_post_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('delete_post', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())