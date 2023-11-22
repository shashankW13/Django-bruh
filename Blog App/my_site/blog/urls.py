from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts', views.AllPostsView.as_view(), name='all-posts'),
    path('posts/<slug:slug>', views.SinglePostView.as_view(), name='post-detail'),
]