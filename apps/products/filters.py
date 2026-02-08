"""
Product filters for category and ordering.
Uses DjangoFilterBackend for efficient filtering.
"""
import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    """Filter products by category, price range, and active status."""
    category = django_filters.CharFilter(field_name='category__slug', lookup_expr='exact')
    category_id = django_filters.NumberFilter(field_name='category__id')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    is_active = django_filters.BooleanFilter(field_name='is_active')

    class Meta:
        model = Product
        fields = ['category', 'category_id', 'min_price', 'max_price', 'is_active']
