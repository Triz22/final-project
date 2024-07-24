from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """ Recipe Form """
    class Meta:
        """ fields for recipe form"""
        model = Post
        fields = ('anime_title', 'description', 'rating',
                  'recommended', 'featured_image')