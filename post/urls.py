from django.urls import path
from . import views


urlpatterns = [
    path('article/', views.ArticleList().as_view(), name='article-list'),
    path('article/latest/', views.LatestArticleList().as_view(), name='latest-article'),
    path('article/<slug>/', views.ArticleDetail().as_view(), name='article-detail'),
    path('article/category/<slug>/', views.CategoryWiseArticleList().as_view(), name='category-wise-article'),

    path('category/', views.CategoryList().as_view(), name='category-list'),

    path('tags/', views.TagList().as_view(), name='tag-list'),
]