from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from .models import Post
from .forms import PostForm

# Create your views here.

class PostList (generic.ListView):
    queryset = Post.objects.all().order_by('-created_on')
    template_name = 'blog/blog_list.html'
    paginate_by = 10


class SharePost(View):
    """ add post"""

    def get(self, request):
        """What happens for a GET request"""
        return render(
            request, "blog/share_post.html", {"post_form": PostForm()})

    def post(self, request):
        """What happens for a POST request"""
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('bloglist')
        else:
            messages.error(self.request, 'Please complete all required fields')
            post_form = PostForm()

        return render(
            request,
            "blog/share_post.html",
            {
                "post_form": post_form

            },
        )
        

def post_detail(request, post_id):
    """ Post detail view"""
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, pk=post_id)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)

    
# class PostDetails(View):
#     """ view for Post Details"""

#     def get(self, request, slug):
#         """What happens for a GET request"""
#         queryset = Post.objects.all()
#         post = get_object_or_404(queryset, slug=slug)
#         context={
#             "post": post,
#         }

#         return render(request,"post_detail.html", context)