from django.shortcuts import render, get_object_or_404
from .models import Post

def get_date(post):
    return post['date']

def index(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/index.html', 
                  context={
                      'posts': latest_posts,
                  })

def all_posts(request):
    all_posts = Post.objects.all().order_by('-date')
    return render(request, 'blog/all-posts.html', 
                  context={
                      'all_posts': all_posts,
                  })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html',
                  context={
                      'post': post,
                      'post_tags': post.tags.all(),
                  })