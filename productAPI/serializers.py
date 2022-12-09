from rest_framework import serializers
from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'productName', 'description', 'dateAdded', 'regularPrice', 'profit', 'supply', 'category','titleImage','image2','image3','image4','get_absolute_url','getTitleImage',
        'getImage2','getImage3','getImage4','thumbnail']

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'get_absolute_url', 'products']