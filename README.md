# Car Management API

A backend REST API for managing cars, users, and sales operations. Built with Flask, SQLAlchemy, and PostgreSQL.

---

## 📌 Overview

This project is a backend system designed to manage a car inventory platform. It supports user authentication, role-based access, and CRUD operations for cars and sales records.

The goal of this project is to demonstrate clean backend architecture, proper database relationships, and production-ready API design.

---

## ⚙️ Tech Stack

* Python 3
* Flask
* Flask-JWT-Extended (Authentication)
* Flask-SQLAlchemy (ORM)
* Flask-Migrate (Database migrations)
* PostgreSQL
* Pytest (Testing)

---

## 📁 Project Structure

```
server/
  app/
    models/        # Database models
    routes/        # API endpoints
    services/      # Business logic
    schemas/       # Data validation / serialization
    extensions/    # DB, JWT, and other extensions setup
    config/        # Configuration settings
  migrations/      # Database migrations
  tests/           # Unit tests
  seed/             # Seed data scripts
  run.py           # Application entry point
```

---

## 🚀 Features

### Authentication

* User registration
* Login with JWT tokens
* Protected routes

### User Management

* Create users
* Role-based access control (e.g., admin vs user)

### Car Management

* Create cars
* Update car details
* Delete cars
* List all available cars

### Sales Management

* Register car sales
* Track ownership changes
* Prevent invalid deletions via foreign key constraints

---

## 🧪 API Endpoints (Examples)

### Auth

* `POST /auth/register` → Register user
* `POST /auth/login` → Login user

### Cars

* `GET /cars` → Get all cars
* `POST /cars/create` → Create a car (protected)
* `PATCH /cars/update/<id>` → Update car
* `DELETE /cars/delete/<id>` → Delete car

### Users

* `GET /users` → Get users (admin only)

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/car-management-api.git
cd car-management-api/server
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup environment variables

Create a `.env` file:

```
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
```

### 5. Run database migrations

```bash
flask db upgrade
```

### 6. Seed database (optional)

```bash
python seed/seed.py
```

### 7. Run the application

```bash
python run.py
```

---

## 🧠 Architecture Notes

* Routes are kept thin and delegate logic to service layer
* Business logic is isolated in `services/`
* Models define database structure
* JWT is used for authentication and route protection
* Migrations are handled using Flask-Migrate

---

## 🧪 Testing

Run tests with:

```bash
pytest
```

---

## 📌 Future Improvements

* Add pagination for car listings
* Improve validation with stricter schemas
* Add Swagger/OpenAPI documentation
* Add CI/CD pipeline with GitHub Actions
* Improve test coverage

---

## 👨‍💻 Author

Built by Alejandro Cabrera as a backend portfolio project focused on API design, database relationships, and authentication systems.
