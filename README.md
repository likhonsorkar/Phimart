# PhiMart

PhiMart is a Django-based e-commerce platform providing a RESTful API for managing products, orders, and users.

## Features

*   **Authentication:** User registration, login, logout, and token refresh.
*   **Product Management:** Create, read, update, and delete products.
*   **Category Management:** Organize products into categories.
*   **Shopping Cart:** Add, update, and remove items from a shopping cart.
*   **Order Management:** Place and track orders.
*   **User Profiles:** Manage user profiles.
*   **Admin Dashboard:** View key metrics like total users, orders, and products.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/phimart.git
    cd phimart
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply the database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

## Usage

1.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

2.  **Access the API at `http://127.0.0.1:8000/`**.

## API Endpoints

| Method | Endpoint                 | Description                  |
| ------ | ------------------------ | ---------------------------- |
| POST   | `/auth/register/`        | Register a new user          |
| POST   | `/auth/login/`           | Log in and obtain a token    |
| POST   | `/auth/logout/`          | Log out the current user     |
| POST   | `/auth/token/refresh/`   | Refresh an expired JWT token |
| GET    | `/api/categories/`       | List all categories          |
| GET    | `/api/products/`         | List all products            |
| POST   | `/api/carts/`            | Create a shopping cart       |
| GET    | `/api/orders/`           | List all orders              |
| GET    | `/api/profile/`          | Get user profile             |

## Project Structure

```
phimart/
├── api/
├── orders/
├── products/
├── users/
└── manage.py
```

## Technologies Used

*   **Backend:** Django, Django REST Framework
*   **Database:** SQLite3 (default)