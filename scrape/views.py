from django.shortcuts import render
from .models import News, IndexPrice
from .serializers import NewsSerializer, IndexPriceSerializer
from rest_framework import generics

class NewsListCreate(generics.ListCreateAPIView):
  queryset = News.objects.all()
  serializer_class = NewsSerializer

class IndexPriceCreate(generics.ListCreateAPIView):
  queryset = IndexPrice.objects.all()
  serializer_class = IndexPriceSerializer
