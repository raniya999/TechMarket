from rest_framework import serializers
from .models import Brand, Category, Phone, Order


class BrandSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100, required=False, allow_blank=True)

    def create(self, validated_data):
        return Brand.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
        return instance


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    slug = serializers.SlugField()

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance


class PhoneSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Phone
        fields = ['id', 'brand', 'brand_name', 'category', 'category_name', 'model_name', 'price', 'description']


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