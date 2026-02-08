# ALX Project Nexus – E-Commerce Backend

Production-ready Django REST API for an e-commerce product catalog. Built for scalability, clean architecture, database performance, and security.

## Tech Stack

| Component | Technology |
|-----------|------------|
| Backend | Django 4.2 + Django REST Framework |
| Database | PostgreSQL |
| Authentication | JWT (djangorestframework-simplejwt) |
| API Docs | Swagger / OpenAPI (drf-yasg) |
| Filtering | django-filter |
| ORM | Django ORM |

## Project Structure

```
ecommerce/
├── config/                 # Project configuration
│   ├── settings/          # base, development, production
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── users/             # Auth & JWT
│   ├── categories/        # Category CRUD
│   └── products/          # Product CRUD, filtering, pagination
├── requirements.txt
├── manage.py
├── Procfile               # Deployment (Render/Railway)
└── README.md
```

## Setup

### Prerequisites

- Python 3.11+
- PostgreSQL 14+

### 1. Clone & Virtual Environment

```bash
cd "alx project"
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Variables

Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
```

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | Django secret key |
| `DB_NAME` | PostgreSQL database name |
| `DB_USER` | PostgreSQL user |
| `DB_PASSWORD` | PostgreSQL password |
| `DB_HOST` | Database host (e.g. localhost) |
| `DB_PORT` | Database port (5432) |

### 4. Database

Create PostgreSQL database and run migrations:

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Run Server

```bash
python manage.py runserver
```

## API Documentation

- **Swagger UI**: `http://localhost:8000/swagger/`
- **ReDoc**: `http://localhost:8000/redoc/`
- **OpenAPI JSON**: `http://localhost:8000/swagger.json/`

## Authentication Flow

1. **Register**  
   `POST /api/auth/register/`

2. **Login**  
   `POST /api/auth/token/`  
   Returns `access` and `refresh` tokens.

3. **Use Token**  
   Add header: `Authorization: Bearer <access_token>`

4. **Refresh**  
   `POST /api/auth/token/refresh/`  
   Body: `{"refresh": "<refresh_token>"}`

### Example: Register

```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john",
    "email": "john@example.com",
    "password": "SecurePass123!",
    "password_confirm": "SecurePass123!"
  }'
```

### Example: Login

```bash
curl -X POST http://localhost:8000/api/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "john", "password": "SecurePass123!"}'
```

### Example: List Products (with filters)

```bash
# All products
curl http://localhost:8000/api/products/

# Filter by category
curl "http://localhost:8000/api/products/?category=electronics"

# Sort by price ascending
curl "http://localhost:8000/api/products/?ordering=price"

# Sort by price descending
curl "http://localhost:8000/api/products/?ordering=-price"

# Pagination
curl "http://localhost:8000/api/products/?page=2&page_size=10"

# Price range
curl "http://localhost:8000/api/products/?min_price=10&max_price=100"
```

## API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/api/auth/register/` | No | Register user |
| POST | `/api/auth/token/` | No | Login (get tokens) |
| POST | `/api/auth/token/refresh/` | Refresh | Refresh access token |
| GET | `/api/auth/me/` | Yes | Current user profile |
| GET | `/api/categories/` | No | List categories |
| POST | `/api/categories/` | Yes | Create category |
| GET | `/api/categories/<slug>/` | No | Category detail |
| PUT/PATCH | `/api/categories/<slug>/` | Yes | Update category |
| DELETE | `/api/categories/<slug>/` | Yes | Delete category |
| GET | `/api/products/` | No | List products (filter, sort, paginate) |
| POST | `/api/products/` | Yes | Create product |
| GET | `/api/products/<slug>/` | No | Product detail |
| PUT/PATCH | `/api/products/<slug>/` | Yes | Update product |
| DELETE | `/api/products/<slug>/` | Yes | Delete product |

## Database Optimization

- **Indexes** on: `category`, `price`, `name`, `created_at`, `is_active` for products; `name`, `slug` for categories.
- **select_related('category')** on product querysets to avoid N+1 queries.
- **Composite index** on `(category, price)` for filtered/sorted product lists.

## Deployment (Render / Railway)

1. Set environment variables in the hosting dashboard.
2. Use `Procfile` for the web process.
3. Use `build.sh` or equivalent for migrations and `collectstatic`.
4. Use `config.settings.production` (`DJANGO_SETTINGS_MODULE`).

### Environment Variables for Production

- `SECRET_KEY`
- `DEBUG=False`
- `ALLOWED_HOSTS` (comma-separated)
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
- `CORS_ALLOWED_ORIGINS` (comma-separated)

## Database Optimization

See [docs/DATABASE_OPTIMIZATION.md](docs/DATABASE_OPTIMIZATION.md) for index and query optimization details.

