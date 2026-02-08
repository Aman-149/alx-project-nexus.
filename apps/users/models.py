"""
User model - Custom user extending AbstractUser.
Supports JWT authentication and role-based access.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model for e-commerce backend.
    Extends AbstractUser for full Django auth compatibility.
    Password hashing handled by Django's built-in PBKDF2 (default).
    """
    email = models.EmailField(unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['email'], name='user_email_idx'),
            models.Index(fields=['username'], name='user_username_idx'),
            models.Index(fields=['created_at'], name='user_created_idx'),
        ]

    def __str__(self):
        return self.email or self.username
