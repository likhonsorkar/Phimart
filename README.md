# PhiMart

PhiMart is a robust e-commerce platform built with Django and Django REST Framework. It provides a full-featured backend for an online store, including user authentication, product management, and order processing.

## Features

*   **User Authentication:** Secure user registration and login system.
*   **Product Catalog:** A comprehensive product management system with support for categories, images, and reviews.
*   **Shopping Cart:** A fully functional shopping cart for a seamless user experience.
*   **Order Management:** An efficient order processing system to manage customer orders.
*   **REST API:** A powerful REST API to interact with the application's data.

## Installation

### Prerequisites

*   Python 3.8+
*   pip

### Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/phimart.git
    cd phimart
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser to access the admin panel:**
    ```bash
    python manage.py createsuperuser
    ```

## Usage

Start the development server:
```bash
python manage.py runserver
```
The application will be available at `http://127.0.0.1:8000`.

## API

PhiMart provides a comprehensive REST API for interacting with the application's data.

### API Documentation

The API is self-documented using Swagger and ReDoc. Once the server is running, you can access the documentation at:

-   **Swagger UI:** `http://127.0.0.1:8000/swagger/`
-   **ReDoc:** `http://127.0.0.1:8000/redoc/`

### Endpoints

Here are some of the main available endpoints:

-   `/api/v1/products/`
-   `/api/v1/products/{product_id}/reviews/`
-   `/api/v1/products/{product_id}/images/`
-   `/api/v1/categories/`
-   `/api/v1/carts/`
-   `/api/v1/carts/{cart_id}/items/`
-   `/api/v1/orders/`
-   `/api/v1/auth/` (for user authentication, includes endpoints like `login`, `logout`, `users`, etc.)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
