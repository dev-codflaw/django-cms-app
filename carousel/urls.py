from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarouselList().as_view(), name='carousel-list'),
    path('<pk>/', views.CarouselDetail().as_view(), name='carousel-detail'),
]