from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Carousel
from .serializers import CarouselSerializer



class CarouselWithTextImage(APIView):

    def get(self, request):
        content = {'message': 'carousel slider'}
        return Response(content)



class CarouselList(APIView):

    def get(self, request):
        queryset = Carousel.objects.all()
        serialized_content = CarouselSerializer(queryset, many=True)
        # content = {'message': 'carousel list'}
        return Response(serialized_content.data)


class CarouselDetail(APIView):
    def get(self, request, pk):
        queryset = Carousel.objects.get(pk=pk)
        serialized_content = CarouselSerializer(queryset)
        return Response(serialized_content.data)