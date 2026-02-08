"""
Category model - Product taxonomy.
Indexed for high-frequency filtering queries.
"""
from django.db import models


class Category(models.Model):
    """
    Product category for taxonomy and filtering.
    One Category -> Many Products.
    """
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(unique=True, db_index=True, max_length=120)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'], name='category_name_idx'),
            models.Index(fields=['slug'], name='category_slug_idx'),
            models.Index(fields=['created_at'], name='category_created_idx'),
        ]

    def __str__(self):
        return self.name
