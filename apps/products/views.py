"""
Product CRUD views with filtering, sorting, and pagination.
Optimized querysets: select_related for category to avoid N+1.
"""
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Product
from .serializers import ProductSerializer, ProductListSerializer
from .filters import ProductFilter
from .pagination import StandardResultsSetPagination


class ProductListCreateView(generics.ListCreateAPIView):
    """
    List products with filtering, sorting, pagination.
    Filter by: category, min_price, max_price, is_active.
    Sort by: price, name, created_at (use ?ordering=price or ?ordering=-price).
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultsSetPagination
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'name', 'created_at']
    ordering = ['-created_at']

    def get_queryset(self):
        # select_related: avoid N+1 when rendering category in list
        return Product.objects.select_related('category').all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductListSerializer
        return ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a product.
    select_related for category in detail view.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Product.objects.select_related('category')
    serializer_class = ProductSerializer
    lookup_field = 'slug'
