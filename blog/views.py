from django.shortcuts import render, redirect
from django.views import generic, View
from django.contrib import messages
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

    def post(self, request):
        if request.method == "POST":
            post_form = PostForm(data=request.POST)
            if post_form.is_valid():
                post_form.save()
                messages.add_message(request, messages.SUCCESS, "Post successfully shared! Thanks for being such a good clan member, the clan appreciates it!")

        return redirect('blog_list')
        

    

