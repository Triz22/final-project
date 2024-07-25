from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """ Share Post Form """
    class Meta:
        """ fields for post form"""
        model = Post
        fields = ('anime_title', 'description', 'rating',
                  'recommended', 'featured_image')

class CommentForm(forms.ModelForm):
    """ Collect user input as comment"""
    class Meta:
        """single body field for comment"""
        model = Comment 
        fields = ('body',)