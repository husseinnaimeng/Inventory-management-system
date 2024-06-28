Inventory Management System Documentation
Introduction

The Inventory Management System is a robust solution built using Django to handle multi-inventory and multi-branch operations. This system includes features such as middleware for logging and security, permissions management, support for wholesale vendors and manufacturers, a basic reporting and analysis module, and a RESTful API for integrations. The system adheres to Object-Oriented Programming (OOP) principles and includes basic security considerations.
Features

    Multi-Inventory and Multi-Branch Management:
        Handle multiple inventories across various branches seamlessly.
        Centralized management and reporting for all branches.

    Middlewares:
        Custom middleware for logging and request processing.
        Security middleware to protect against common vulnerabilities.

    Permissions:
        Role-based access control.
        Fine-grained permissions for different user roles.

    Wholesale Vendors and Manufacturers:
        Manage relationships with wholesale vendors and manufacturers.
        Track purchase orders, shipments, and payments.

    Basic Reporting System and Analysis:
        Generate basic reports on inventory levels, sales, and branch performance.
        Analyze trends and make informed decisions.

    Logging:
        Comprehensive logging of system activities for audit and troubleshooting.

    RESTful API:
        API endpoints for integrating with other systems and applications.
        Secure and scalable API design.

    Object-Oriented Programming (OOP):
        Clean and maintainable codebase using OOP principles.

    Basic Security Considerations:
        User authentication and authorization.
        Protection against CSRF, XSS, and SQL injection attacks.


Problems and basic data strcture implementation

- [Mutiply Product Types](./inventory/Multiple%20Product%20Type.md)

Installation

    Clone the repository:

```bash

git clone https://github.com/husseinnaimeng/Inventory-management-system.git

cd inventory-management-system
```
Create a virtual environment:


```bash
python3 -m venv env
source env/bin/activate

```
Install dependencies:

```bash

pip install -r requirements.txt


```
Apply migrations:

```bash

python manage.py migrate


```
Create a superuser:

```bash

python manage.py createsuperuser


```
Run the development server:

```bash

python manage.py runserver
```