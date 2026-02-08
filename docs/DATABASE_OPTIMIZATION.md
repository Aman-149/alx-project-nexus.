# Database Optimization Documentation

This document explains the database optimizations applied to the Nexus E-commerce backend.

## Indexes

### User Model (`apps.users.models.User`)
- **email_idx**: Filters and lookups by email (login, uniqueness checks).
- **username_idx**: Filters and lookups by username.
- **created_at_idx**: Ordering user lists by registration date.

### Category Model (`apps.categories.models.Category`)
- **category_name_idx**: Filtering and search by category name.
- **category_slug_idx**: Lookups by slug (detail views, product filtering).
- **category_created_idx**: Sorting categories by creation date.

### Product Model (`apps.products.models.Product`)
- **product_category_idx**: High-frequency filter—products by category.
- **product_price_idx**: Sorting by price (asc/desc).
- **product_name_idx**: Search and filtering by product name.
- **product_created_idx**: Sorting product lists by date.
- **product_active_idx**: Filtering active/inactive products.
- **product_category_price_idx**: Composite index for `category + price`—optimizes filtered and sorted product lists in a single index scan.

## Query Optimization

### select_related
Used in product querysets to avoid N+1 queries:
- **ProductListCreateView**: `Product.objects.select_related('category')` — each product has one category; prefetch in one JOIN.
- **ProductDetailView**: Same—category is serialized in detail response.

### prefetch_related
Not required for current schema—products have a single category (ForeignKey), not reverse many-to-many. If we add tags or related products later, we would use `prefetch_related('tags')` or similar.

### Filter Backends
- **DjangoFilterBackend**: Uses indexed fields (category, price) for efficient WHERE clauses.
- **OrderingFilter**: Uses indexed fields (price, name, created_at) for ORDER BY.

## Pagination
- **PageNumberPagination**: Predictable page numbers for frontend.
- **page_size**: 20 default, max 100 to limit result sets and memory use.
