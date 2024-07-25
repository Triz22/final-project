from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class News(models.Model):
    news_title = models.CharField(max_length=200, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

class Post(models.Model):

    RATING = [
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    ]

    anime_title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
        )
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=RATING,default=1)
    recommended = models.BooleanField(default=True)
    likes = models.ManyToManyField(User,related_name='blog_likes',blank=True)

    def __str__(self):
        return f"The anime I am currently watching is {self.anime_title} !!!"


    def get_absolute_url(self):
        """Sets absolute URL"""
        return reverse('bloglist')
       

class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,max_length=70)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments_post_name')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)