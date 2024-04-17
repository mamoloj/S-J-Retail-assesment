# Project Name

## Description
This Django project serves as a backend for managing products and user signups. It provides API endpoints for creating, retrieving, updating, and deleting products, as well as signing up users.

## Installation
1. Clone this repository to your local machine:
    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:
    ```bash
    cd <project-directory>
    ```

3. Create a virtual environment:
    ```bash
    py -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

5. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

6. Apply migrations to set up the database:
    ```bash
    python manage.py migrate
    ```

## Usage
1. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

2. Access the API endpoints:
    - **Products:**
        - List all products: `GET /products/`
        - Retrieve a product by ID: `GET /products/<id>/`
        - Create a new product: `POST /products/`
        - Update an existing product: `PUT /products/<id>/` or `PATCH /products/<id>/`
        - Delete a product: `DELETE /products/<id>/`

    - **User Signup:**
        - Signup a new user: `POST /signup/`


3. Access API documentation:
    - **Swagger UI:** `http://localhost:8000/swagger/`
    - **Redoc:** `http://localhost:8000/api-docs/`

## Authentication
- API endpoints for products require authentication using JSON Web Tokens (JWT).
- You need to signup first to create your account using `http://localhost:8000/signup/`
- Obtain JWT by sending a POST request to `http://localhost:8000/api/token/` with valid user credentials.
- Use the obtained token in the Authorization header for authenticated requests:
    ```http
    Authorization: Bearer <token>
    ```

