from django.shortcuts import render
from django.views import generic, View
from .models import Post
from .forms import PostForm

# Create your views here.

class PostList (generic.ListView):
    queryset = Post.objects.all()
    template_name = 'blog/blog_list.html'
    paginate_by = 10


class SharePost(View):
    """ add post"""
    def get(self, request):
        """What happens for a GET request"""
        return render(
            request, "blog/share_post.html", {"post_form": PostForm()})

