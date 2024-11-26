from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer() # Nested serializer for category

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category']

