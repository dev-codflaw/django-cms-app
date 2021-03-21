from django.urls import path
from . import views


urlpatterns = [
    path('posts/latest/', views.LatestPostList().as_view(), name='post-list'),
    path('posts/', views.PostList().as_view(), name='post-list'),
    path('posts/<slug>/', views.PostDetail().as_view(), name='post-detail'),

    path('categories/', views.CategoryList().as_view(), name='category-list'),

    path('tags/', views.TagList().as_view(), name='tag-list'),
]