# FastAPI E-Commerce

Welcome to the FastAPI E-Commerce project! This project is a modern e-commerce platform built with FastAPI and SQLAlchemy, designed to provide a seamless online shopping experience.

## Features

- **Product Management**: Create, read, update, and delete products with various attributes such as title, description, price, discount, rating, and images.
- **Category Management**: Organize products into categories for easier browsing.
- **User Authentication**: Secure user authentication and authorization with role management.
- **Shopping Cart**: Add products to the shopping cart and manage items.
- **Order Processing**: Complete the checkout process and manage orders.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.10+.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **PostgreSQL**: Advanced open-source relational database.
- **Alembic**: Database migration tool for SQLAlchemy.
- **Docker**: Containerization for consistent development and deployment environments.

## Installation

To get started with the FastAPI E-Commerce project, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/abduvalimurodullayev1/fastapi_e-commerce.git
   cd fastapi_e-commerce
2.python -m venv venv


3. **venv\Scripts\activate
source venv/bin/activate
4. ** pip install -r requirements.txt
5.alembic upgrade head
6.uvicorn app.main:app --reload




Models
User
id: Unique identifier for the user.
username: Unique username for login.
email: Unique email address.
password: User password (hashed).
full_name: Full name of the user.
is_active: Boolean flag indicating if the user is active.
created_at: Timestamp of user creation.
role: Role of the user (admin or user).
carts: Relationship with carts.
Cart
id: Unique identifier for the cart.
user_id: Foreign key to the user.
created_at: Timestamp of cart creation.
total_amount: Total amount for the cart.
user: Relationship with the user.
cart_items: Relationship with cart items.
CartItem
id: Unique identifier for the cart item.
cart_id: Foreign key to the cart.
product_id: Foreign key to the product.
quantity: Quantity of the product in the cart.
subtotal: Subtotal amount for this item.
cart: Relationship with the cart.
product: Relationship with the product.
Category
id: Unique identifier for the category.
name: Name of the category.
products: Relationship with products.
Product
id: Unique identifier for the product.
title: Title of the product.
description: Description of the product.
price: Price of the product.
discount_percentage: Discount percentage on the product.
rating: Rating of the product.
stock: Stock quantity of the product.
brand: Brand of the product.
thumbnail: Thumbnail image URL of the product.
images: List of image URLs for the product.
is_published: Boolean flag indicating if the product is published.
created_at: Timestamp of product creation.
category_id: Foreign key to the category.
category: Relationship with the category.
cart_items: Relationship with cart items.
Configuration
Database Configuration: Modify the sqlalchemy.url in alembic.ini to match your database settings.
Environment Variables: Use environment variables to manage sensitive data such as secret keys and database URLs.
Usage
API Documentation: Access the interactive API documentation at http://localhost:8000/docs.
Contributing
We welcome contributions to this project! Please follow these guidelines:

Fork the repository.
Create a new branch for your feature or fix.
Commit your changes with descriptive messages.
Open a pull request with a clear description of your changes.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For questions or feedback, please open an issue on GitHub or contact the maintainer:

Abduvali Murodullayev
GitHub Profile
Thank you for checking out the FastAPI E-Commerce project!
