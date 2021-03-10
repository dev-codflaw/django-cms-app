from rest_framework import serializers
from .models import Post, Category, Tag


class PostSerializer(serializers.ModelSerializer):
    # description = serializers.SerializerMethodField()

    # def get_description(self, instance):
    #     from django.utils.safestring import mark_safe
    #     return mark_safe(instance.description)

    class Meta:
        model = Post
        fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields ='__all__'