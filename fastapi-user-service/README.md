# FastAPI User Service

## Overview

This project is a backend REST API service built using **FastAPI**, **PostgreSQL**, and **SQLAlchemy (async ORM)**.

The service provides basic **CRUD operations for users**, along with common backend features such as **health checks** and **pagination**, following clean architecture and RESTful design principles.



## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy (async)
- Pydantic
- Uvicorn
- pgAdmin
- Git



## Architecture Overview

The project follows a layered architecture:

- **API Layer**  
  Handles HTTP requests and responses. Contains no business logic.

- **CRUD Layer**  
  Contains business rules and database operations. Raises domain-specific exceptions.

- **Models**  
  SQLAlchemy ORM models that define database tables.

- **Schemas**  
  Pydantic models that define request and response JSON structures.

- **Exception Layer**  
  Centralized exception definitions and handlers to map errors to HTTP responses.

- **Core Utilities**  
  Configuration and logging shared across the application.



## Running the Application

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize database (first run)
python -m app.db.init_db

# Start the server
uvicorn app.main:app --reload
```



## User Management API Contract

## Overview
This document defines the REST API contract for the User Management Service.

## Create User

### Endpoint
	POST /users

### Headers
- Content-Type: application/json

### Request
	{
	  "name": "string",
	  "email": "string"
	}

### Response
	{
	  "id": number,
	  "name": "string",
	  "email": "string",
	  "is_active": boolean,
	  "created_at": "string",
	  "updated_at": "string"
	}

### Status Codes
- 201 Created
- 409 Conflict
- 422 Unprocessable Entity



## Get All Users (Paginated)

### Endpoint
	GET /users

### Query Parameters
- skip : number (default: 0)
- limit : number (default: 10)

### Response
	[
	  {
	    "id": number,
	    "name": "string",
	    "email": "string",
	    "is_active": boolean,
	    "created_at": "string",
	    "updated_at": "string"
	  },
	  {
	    "id": number,
	    "name": "string",
	    "email": "string",
	    "is_active": boolean,
	    "created_at": "string",
	    "updated_at": "string"
	  }
	]

### Status Codes
- 200 OK
- 500 Internal Server Error



## Get User by ID

### Endpoint
	GET /users/{id}

### Route Params
- id : number (User ID)

### Response
	{
	  "id": number,
	  "name": "string",
	  "email": "string",
	  "is_active": boolean,
	  "created_at": "string",
	  "updated_at": "string"
	}

### Status Codes
- 200 OK
- 404 Not Found



## Update User (Full Update)

### Endpoint
	PUT /users/{id}

### Route Params
- id : number (User ID)

### Headers
- Content-Type: application/json

### Request
	{
	  "name": "string",
	  "email": "string",
	  "is_active": boolean
	}

### Response
	{
	  "id": number,
	  "name": "string",
	  "email": "string",
	  "is_active": boolean,
	  "created_at": "string",
	  "updated_at": "string"
	}

### Status Codes
- 200 OK
- 404 Not Found
- 422 Unprocessable Entity



## Update User (Partial Update)

### Endpoint
	PATCH /users/{id}

### Route Params
- id : number (User ID)

### Headers
- Content-Type: application/json

### Request
	{
	  "email": "string"
	}

### Response
	{
	  "id": number,
	  "name": "string",
	  "email": "string",
	  "is_active": boolean,
	  "created_at": "string",
	  "updated_at": "string"
	}

### Status Codes
- 200 OK
- 404 Not Found
- 422 Unprocessable Entity



## Delete User

### Endpoint
	DELETE /users/{id}

### Route Params
- id : number (User ID)

### Status Codes
- 204 No Content
- 404 Not Found



## Health Check

### Endpoint
	GET /health

### Response
	{
	  "status": "ok"
	}

### Status Codes
- 200 OK

