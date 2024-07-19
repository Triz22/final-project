from django.shortcuts import render,HttpResponse

# Create your views here.

def get_blog_list(request):
    return render(request, 'blog/blog_list.html')

