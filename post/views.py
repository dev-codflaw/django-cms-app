from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, Category, Tag
from .serializers import PostSerializer, CategorySerializer, TagSerializer
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

class ArticleList(APIView):
    # permission_classes = (AllowAny)

    def get(self, request):
        queryset = Post.objects.all()
        serialized_content = PostSerializer(queryset, many=True)
        # print(serializer.data)
        # content = {'data': 'post content'}
        return Response(serialized_content.data)

    @csrf_exempt
    def post(self, request):
        print(request.data)
        serialized_content = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # content = {'data': 'post content'}

        return Response(request.data)


class LatestArticleList(APIView):
    # permission_classes = (AllowAny)

    def get(self, request):
        queryset = Post.objects.all().order_by('-id')[:10]
        serialized_content = PostSerializer(queryset, many=True)
        # print(serializer.data)
        # content = {'data': 'post content'}
        return Response(serialized_content.data)
    


class ArticleDetail(APIView):

    def get(self, request, slug):
        queryset = Post.objects.get(slug=slug)
        serialized_content = PostSerializer(queryset)
        # content = {'slug': slug}
        return Response(serialized_content.data)




class CategoryList(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        serialized_content = CategorySerializer(queryset, many=True)
        # content = {'category': 'all categories'}
        return Response(serialized_content.data)


class CategoryWiseArticleList(APIView):
    def get(self, request, slug):
        queryset = Post.objects.filter(category__slug=slug)
        serialized_content = PostSerializer(queryset, many=True)
        return Response(serialized_content.data)



class TagList(APIView):
    def get(self, request):
        queryset = Tag.objects.all()
        serialized_content = TagSerializer(queryset, many=True)
        return Response(serialized_content.data)