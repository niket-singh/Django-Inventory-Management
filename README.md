# Inventory Management API

## Setup Instructions
1. Clone the repository
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Create superuser: `python manage.py createsuperuser`
6. Run server: `python manage.py runserver`

## API Endpoints
- `/api/products/`: List and create products
- `/api/products/{id}/`: Retrieve, update, delete specific product
- `/api/products/out_of_stock/`: List out-of-stock products
- `/api/products/{id}/update_stock/`: Update product stock
- `/api/categories/`: List and create categories

## Features
- Product Management
- Stock Tracking
- Category Management