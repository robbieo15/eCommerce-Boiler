from rest_framework import serializers
from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'productName', 'description', 'dateAdded', 'regularPrice', 'profit', 'supply', 'category','titleImage','image2','image3','image4']
