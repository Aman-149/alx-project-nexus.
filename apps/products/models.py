"""
Product model - E-commerce product catalog.
Indexed for filtering (category, price), sorting, and list queries.
"""
from django.db import models
from apps.categories.models import Category


class Product(models.Model):
    """
    Product in the catalog.
    Many Products -> One Category.
    Indexes optimize: category filter, price sort, name search, created_at sort.
    """
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        db_index=True,
    )
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(unique=True, db_index=True, max_length=280)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['category'], name='product_category_idx'),
            models.Index(fields=['price'], name='product_price_idx'),
            models.Index(fields=['name'], name='product_name_idx'),
            models.Index(fields=['created_at'], name='product_created_idx'),
            models.Index(fields=['is_active'], name='product_active_idx'),
            # Composite index for common filter+order: category + price
            models.Index(
                fields=['category', 'price'],
                name='product_category_price_idx',
            ),
        ]

    def __str__(self):
        return self.name
