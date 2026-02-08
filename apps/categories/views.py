"""
Category CRUD views - RESTful endpoints.
"""
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Category
from .serializers import CategorySerializer, CategoryListSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    """
    List all categories or create a new one.
    GET: public, POST: authenticated only.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategoryListSerializer
        return CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a category.
    GET: public, PUT/PATCH/DELETE: authenticated only.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
