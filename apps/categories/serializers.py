"""
Category serializers for CRUD operations.
"""
from django.utils.text import slugify
from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Full category serializer for create/update/retrieve."""
    slug = serializers.SlugField(required=False, allow_blank=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'description', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

    def validate_slug(self, value):
        if not value:
            return value
        qs = Category.objects.filter(slug=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError('A category with this slug already exists.')
        return value

    def create(self, validated_data):
        if not validated_data.get('slug'):
            base_slug = slugify(validated_data['name'])
            slug = base_slug
            n = 1
            while Category.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{n}'
                n += 1
            validated_data['slug'] = slug
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'name' in validated_data and not validated_data.get('slug'):
            validated_data['slug'] = slugify(validated_data['name'])
        return super().update(instance, validated_data)


class CategoryListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for list views."""

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')
