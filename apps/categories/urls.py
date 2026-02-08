"""
Category API URLs.
"""
from django.urls import path
from .views import CategoryListCreateView, CategoryDetailView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
]
