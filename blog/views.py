from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.views.generic import UpdateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Post
from .forms import PostForm, CommentForm

# Create your views here.


class HomePage(View):
    """
    Home page view
    """
    def get(self, request):
        return render(request, 'blog/index.html')

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
    comments = post.comments_post_name.all().order_by("-created_on")
    liked = False
    if post.likes.filter(id=self.request.user.id).exists():
            liked = True



    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,'Comment submitted, thanks for sharing!'
            )

    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comment_form':comment_form,
        'comments':comments
    }
    return render(request, 'blog/post_detail.html', context)


class EditPost(UpdateView):
    """ Edit Post """
    model = Post
    template_name = 'blog/edit_post.html'
    form_class = PostForm

class PostLike(View):
    """
    Like and unlike post class based view
    """

    def post(self, request,post_id):
         
         post = get_object_or_404(Post, id=post_id)

         if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
         else:
            post.likes.remove(request.user)
         return HttpResponseRedirect(reverse('post_detail', args=[post_id]))      
