from django.contrib import admin
from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price') # Customize displayed fields
    list_filter = ('category',)  # Add a filter for categories
    search_fields = ('name', 'description') # Add search fields

admin.site.register(Category)
admin.site.register(Product, ProductAdmin) 