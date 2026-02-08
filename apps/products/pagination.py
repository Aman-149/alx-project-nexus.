"""
Pagination classes for product catalog.
PageNumberPagination for predictable page-based navigation.
"""
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    """
    Standard page-based pagination.
    Use for product list - predictable page numbers for frontend.
    """
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100
