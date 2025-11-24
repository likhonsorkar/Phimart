# PhiMart Planning

## REST API Endpoints (Table Formatted)

### 1. Authentication Endpoints

  |Method |  Endpoint              |   Description|
  -------- ------------------------ ------------------------------
  |POST   |  `/auth/register/`     |   Register a new user |
  POST     `/auth/login/`           Log in and obtain a token
  POST     `/auth/logout/`          Log out the current user
  POST     `/auth/token/refresh/`   Refresh an expired JWT token

------------------------------------------------------------------------

### 2. Category Endpoints

  Method   Endpoint                  Description
  -------- ------------------------- -------------------------
  GET      `/api/categories/`        List all categories
  GET      `/api/categories/<id>/`   Retrieve a category
  POST     `/api/categories/`        Create category (Admin)
  PUT      `/api/categories/<id>/`   Update category
  DELETE   `/api/categories/<id>/`   Delete category

------------------------------------------------------------------------

### 3. Product Endpoints

  Method   Endpoint                     Description
  -------- ---------------------------- ------------------------
  GET      `/api/products/`             List all products
  GET      `/api/products/<id>/`        Retrieve product
  GET      `/api/products/?search=`     Search products
  POST     `/api/products/`             Create product (Admin)
  PUT      `/api/products/<id>/`        Update product (Admin)
  DELETE   `/api/products/<id>/`        Delete product (Admin)
  GET      `/api/products/?category=`   Filter by category

------------------------------------------------------------------------

### 4. Shopping Cart Endpoints

  Method   Endpoint                                  Description
  -------- ----------------------------------------- ---------------
  POST     `/api/carts/`                             Create a cart
  GET      `/api/carts/<cart_id>/`                   Get a cart
  DELETE   `/api/carts/<cart_id>/`                   Delete a cart
  POST     `/api/carts/<cart_id>/items/`             Add item
  PATCH    `/api/carts/<cart_id>/items/<item_id>/`   Update item
  DELETE   `/api/carts/<cart_id>/items/<item_id>/`   Delete item

------------------------------------------------------------------------

### 5. Order Endpoints

  Method   Endpoint                     Description
  -------- ---------------------------- -----------------------
  GET      `/api/orders/`               List all orders
  GET      `/api/orders/<id>/`          Retrieve order
  POST     `/api/orders/`               Place order
  PUT      `/api/orders/<id>/status/`   Update status (Admin)
  DELETE   `/api/orders/<id>/`          Cancel order

------------------------------------------------------------------------

### 6. Profile Endpoints

  Method   Endpoint          Description
  -------- ----------------- ----------------
  GET      `/api/profile/`   Get profile
  PUT      `/api/profile/`   Update profile

------------------------------------------------------------------------

### 7. Admin Dashboard Endpoints

  Method   Endpoint                           Description
  -------- ---------------------------------- ----------------
  GET      `/api/dashboard/total-users/`      Total users
  GET      `/api/dashboard/total-orders/`     Total orders
  GET      `/api/dashboard/total-products/`   Total products

------------------------------------------------------------------------

## Models (Table Format)

### User Model

  Field          Type          Description
  -------------- ------------- -----------------
  id             Primary Key   Unique ID
  first_name     CharField     First name
  last_name      CharField     Last name
  email          EmailField    Unique email
  address        TextField     Address
  phone_number   CharField     Phone number
  password       CharField     Hashed password

------------------------------------------------------------------------

### Category Model

  Field         Type          Description
  ------------- ------------- ----------------------
  id            Primary Key   Unique ID
  name          CharField     Category name
  description   TextField     Optional description

**Relationship**: One-to-Many → Product

------------------------------------------------------------------------

### Product Model

  Field         Type            Description
  ------------- --------------- -------------------
  id            PK              Unique ID
  name          CharField       Product name
  description   TextField       Description
  price         DecimalField    Price
  stock         IntegerField    Stock count
  image         ImageField      Optional
  category      ForeignKey      Category
  created_at    DateTimeField   Created timestamp
  updated_at    DateTimeField   Updated timestamp

------------------------------------------------------------------------

### Cart Model

  Field        Type            Description
  ------------ --------------- -------------------
  id           PK              Unique ID
  user         OneToOneField   User
  created_at   DateTimeField   Created timestamp

------------------------------------------------------------------------

### CartItem Model

  Field      Type           Description
  ---------- -------------- -------------
  id         PK             Unique ID
  cart       ForeignKey     Cart
  product    ForeignKey     Product
  quantity   IntegerField   Quantity

------------------------------------------------------------------------

### Order Model

  Field         Type            Description
  ------------- --------------- -------------------
  id            PK              Unique ID
  user          ForeignKey      User
  status        CharField       Order status
  total_price   DecimalField    Total price
  created_at    DateTimeField   Created timestamp
  updated_at    DateTimeField   Updated timestamp

------------------------------------------------------------------------

### OrderItem Model

  Field      Type           Description
  ---------- -------------- -------------------
  id         PK             Unique ID
  order      ForeignKey     Order
  product    ForeignKey     Product
  quantity   IntegerField   Ordered quantity
  price      DecimalField   Price at purchase

------------------------------------------------------------------------

## Relationship Summary (Table)

  Model      Relationship
  ---------- ---------------------------------------------
  User       One-to-One → Cart, Many-to-One → Order
  Category   One-to-Many → Product
  Product    Many-to-One → Category, CartItem, OrderItem
  Cart       One-to-Many → CartItem
  Order      One-to-Many → OrderItem
