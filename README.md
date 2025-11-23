# PhiMart – E-commerce API Planning

## 1. Authentication Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /auth/register/ | Register a new user |
| POST | /auth/login/ | Log in and obtain a token |
| POST | /auth/logout/ | Log out the current user |
| POST | /auth/token/refresh/ | Refresh an expired JWT token |

## 2. Category Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/categories/ | List all categories |
| GET | /api/categories/<id>/ | Retrieve category |
| POST | /api/categories/ | Create category (Admin) |
| PUT | /api/categories/<id>/ | Update category |
| DELETE | /api/categories/<id>/ | Delete category |

## 3. Product Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/products/ | List all products |
| GET | /api/products/<id>/ | Get product |
| GET | /api/products/?search= | Search products |
| GET | /api/products/?category= | Filter by category |
| POST | /api/products/ | Create product (Admin) |
| PUT | /api/products/<id>/ | Update product (Admin) |
| DELETE | /api/products/<id>/ | Delete product (Admin) |

## 4. Cart Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/carts/ | Create cart |
| GET | /api/carts/<cart_id>/ | Get cart |
| DELETE | /api/carts/<cart_id>/ | Delete cart |
| POST | /api/carts/<cart_id>/items/ | Add item |
| PATCH | /api/carts/<cart_id>/items/<item_id>/ | Update item |
| DELETE | /api/carts/<cart_id>/items/<item_id>/ | Delete item |

## 5. Order Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/orders/ | List orders |
| GET | /api/orders/<id>/ | Get order |
| POST | /api/orders/ | Create order |
| PUT | /api/orders/<id>/status/ | Update order status (Admin) |
| DELETE | /api/orders/<id>/ | Cancel order |

## 6. Profile Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/profile/ | Get profile |
| PUT | /api/profile/ | Update profile |

## 7. Dashboard Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/dashboard/total-users/ | Total users |
| GET | /api/dashboard/total-orders/ | Total orders |
| GET | /api/dashboard/total-products/ | Total products |
