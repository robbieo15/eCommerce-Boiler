from rest_framework import viewsets
from .models import *
from .serializers import *
from django.shortcuts import render

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def home(req):
    return HttpResponse('Hello')