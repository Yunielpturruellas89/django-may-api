from rest_framework import serializers
from .models import Rating
from apps.product.serializers import ProductSerializer #Import ProductSerializer

class RatingSerializer(serializers.ModelSerializer):
    product = ProductSerializer() #Nested serializer to include product details
    class Meta:
        model = Rating
        fields = ['id', 'user', 'product', 'rating', 'review', 'created_at']
        read_only_fields = ['created_at'] #created_at should not be writable by client

