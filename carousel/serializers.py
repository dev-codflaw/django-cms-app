from rest_framework import serializers
from .models import Carousel, CarouselSlide


class CarouselSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselSlide
        fields = '__all__'


class CarouselSerializer(serializers.ModelSerializer):
    images = CarouselSlideSerializer(many=True, read_only=True)

    class Meta:
        model = Carousel
        fields = '__all__'