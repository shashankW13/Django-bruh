from django.shortcuts import render
from .models import Blog

def index(request):
    blog = Blog.objects.all()
    return render(request, 'blog/index.html', 
                  context={
                      'blogs': blog,
                  })

def all_posts(request):
    blog = Blog.objects.all()
    return render(request, 'blog/posts.html', 
                  context={
                      'blogs': blog,
                  })