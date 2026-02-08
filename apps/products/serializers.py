"""
Product serializers for CRUD and list views.
"""
from django.utils.text import slugify
from rest_framework import serializers
from apps.categories.serializers import CategoryListSerializer
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Full product serializer for create/update/retrieve."""
    category_detail = CategoryListSerializer(source='category', read_only=True)
    slug = serializers.SlugField(required=False, allow_blank=True)

    class Meta:
        model = Product
        fields = (
            'id', 'category', 'category_detail', 'name', 'slug', 'description',
            'price', 'stock', 'is_active', 'created_at', 'updated_at',
        )
        read_only_fields = ('created_at', 'updated_at')

    def validate_slug(self, value):
        if not value:
            return value
        qs = Product.objects.filter(slug=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError('A product with this slug already exists.')
        return value

    def create(self, validated_data):
        if not validated_data.get('slug'):
            base_slug = slugify(validated_data['name'])
            slug = base_slug
            n = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{n}'
                n += 1
            validated_data['slug'] = slug
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'name' in validated_data and not validated_data.get('slug'):
            validated_data['slug'] = slugify(validated_data['name'])
        return super().update(instance, validated_data)


class ProductListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for list views with category name."""
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'slug', 'price', 'stock', 'is_active',
            'category_name', 'created_at',
        )
