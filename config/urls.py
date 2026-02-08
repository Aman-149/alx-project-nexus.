"""
Nexus E-commerce Backend - Main URL Configuration.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger/OpenAPI schema
schema_view = get_schema_view(
    openapi.Info(
        title="Nexus E-commerce API",
        default_version='v1',
        description="""
## E-commerce Product Catalog API

Production-ready REST API for an e-commerce product catalog with:
- **JWT Authentication**: Register, login, token refresh
- **Products & Categories**: Full CRUD with filtering, sorting, pagination
- **Optimized Queries**: Indexed fields, select_related/prefetch_related

### Authentication Flow
1. Register: `POST /api/auth/register/`
2. Login: `POST /api/auth/token/` → Receive `access` and `refresh` tokens
3. Use token: `Authorization: Bearer <access_token>`
4. Refresh: `POST /api/auth/token/refresh/` when access token expires
        """,
        contact=openapi.Contact(email="api@nexus.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # API v1
    path('api/auth/', include('apps.users.urls')),
    path('api/', include('apps.categories.urls')),
    path('api/', include('apps.products.urls')),

    # Swagger Documentation
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
