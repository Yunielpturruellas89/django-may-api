from rest_framework import serializers
from .models import Product
from category.serializers import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer() # Nested serializer for category

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category']

