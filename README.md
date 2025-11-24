# PhiMart Planning

## REST API Endpoints

### 1. Authentication Endpoints

  HTTP Method   Endpoint               Description
  ------------- ---------------------- -------------------------------
  POST          /auth/register/        Register a new user.
  POST          /auth/login/           Log in and obtain a token.
  POST          /auth/logout/          Log out the current user.
  POST          /auth/token/refresh/   Refresh an expired JWT token.

### 2. Category Endpoints

  HTTP Method   Endpoint                         Description
  ------------- -------------------------------- --------------------------------
  GET           /api/categories/                 List all categories.
  GET           /api/categories/`<id>`{=html}/   Retrieve a specific category.
  POST          /api/categories/                 Create a new category (Admin).
  PUT           /api/categories/`<id>`{=html}/   Update a category.
  DELETE        /api/categories/`<id>`{=html}/   Delete a category.

### 3. Product Endpoints

  --------------------------------------------------------------------------------
  HTTP Method             Endpoint                       Description
  ----------------------- ------------------------------ -------------------------
  GET                     /api/products/                 List all products.

  GET                     /api/products/`<id>`{=html}/   Retrieve a specific
                                                         product.

  GET                     /api/products/?search=         Search products by name
                                                         or description.

  POST                    /api/products/                 Create a new product
                                                         (Admin).

  PUT                     /api/products/`<id>`{=html}/   Update a product (Admin).

  DELETE                  /api/products/`<id>`{=html}/   Delete a product (Admin).

  GET                     /api/products/?category=       Filter products by
                                                         category.
  --------------------------------------------------------------------------------

### 4. Shopping Cart Endpoints

  HTTP Method   Endpoint                                                  Description
  ------------- --------------------------------------------------------- ------------------
  POST          /api/carts/                                               Create a cart
  GET           /api/carts/`<cart_id>`{=html}/                            Get a cart
  DELETE        /api/carts/`<cart_id>`{=html}/                            Delete a cart
  POST          /api/carts/`<cart_id>`{=html}/items/                      Add item to cart
  PATCH         /api/carts/`<cart_id>`{=html}/items/`<item_id>`{=html}/   Update an item
  DELETE        /api/carts/`<cart_id>`{=html}/items/`<item_id>`{=html}/   Delete an item

### 5. Order Endpoints

  HTTP Method   Endpoint                            Description
  ------------- ----------------------------------- -----------------------------------
  GET           /api/orders/                        List all orders for current user.
  GET           /api/orders/`<id>`{=html}/          Retrieve a specific order.
  POST          /api/orders/                        Place a new order.
  PUT           /api/orders/`<id>`{=html}/status/   Update order status (Admin).
  DELETE        /api/orders/`<id>`{=html}/          Cancel an order.

### 6. User Profile Endpoints

  HTTP Method   Endpoint        Description
  ------------- --------------- ------------------------
  GET           /api/profile/   Retrieve user profile.
  PUT           /api/profile/   Update user profile.

### 7. Admin Dashboard Endpoints

  HTTP Method   Endpoint                         Description
  ------------- -------------------------------- ---------------------------
  GET           /api/dashboard/total-users/      Total registered users.
  GET           /api/dashboard/total-orders/     Total orders placed.
  GET           /api/dashboard/total-products/   Total available products.

------------------------------------------------------------------------

## Models

### 1. User Model

-   **id**: Primary Key\
-   **first_name**: CharField\
-   **last_name**: CharField\
-   **email**: EmailField\
-   **address**: TextField\
-   **phone_number**: CharField\
-   **password**: CharField (hashed)

### 2. Category Model

-   **id**: Primary Key\
-   **name**: CharField\
-   **description**: TextField (optional)

Relationship: One-to-Many with Product

### 3. Product Model

-   **id**, **name**, **description**, **price**, **stock**, **image**,
    **category**, **created_at**, **updated_at**

### 4. Cart Model

-   **id**, **user**, **created_at**

Relationship: One-to-One with User

### 5. CartItem Model

-   **id**, **cart**, **product**, **quantity**

Relationships: Many-to-One with Cart, Product

### 6. Order Model

-   **id**, **user**, **status**, **total_price**, **created_at**,
    **updated_at**

### 7. OrderItem Model

-   **id**, **order**, **product**, **quantity**, **price**

------------------------------------------------------------------------

## Relationship Summary

-   User: One-to-One with Cart, Many-to-One with Order\
-   Category: One-to-Many with Product\
-   Product: Many-to-One with Category, CartItem, OrderItem\
-   Cart: One-to-Many with CartItem\
-   Order: One-to-Many with OrderItem
