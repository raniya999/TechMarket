from rest_framework import serializers
from .models import Brand, Category, Phone, Order

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'country']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'icon']


class PhoneSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Phone
        fields = [
            'id', 'brand', 'brand_name', 'category', 'category_name',
            'name', 'price', 'old_price', 'memory_gb', 'description',
            'short_description', 'specifications', 'image', 'rating',
            'stock', 'sold_count', 'in_stock', 'created_at',
        ]


class OrderSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    phone_name = serializers.CharField(source='phone.name', read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'user', 'username', 'phone', 'phone_name',
            'quantity', 'status', 'created_at',
        ]
        read_only_fields = ['id', 'user', 'created_at']
