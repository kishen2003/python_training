# Student Management API Contract

## Overview
This document defines the REST API contract for the Student Management System.

## Base URL
/api

---

## Create Student

### Endpoint
    POST /students

### Headers
- Content-Type: application/json

### Request
```json
{
  "name": "string",
  "roll_no": "string",
  "department": "string",
  "email": "string"
}
```

### Response
```json
{
  "id": number,
  "name": "string",
  "roll_no": "string",
  "department": "string",
  "email": "string"
}
```

### Status Codes
- 201 Created
- 400 Bad Request

## Get all students

### Endpoint
    GET /students

### Response
```json
[
  {
    "id": number,
    "name": "string",
    "roll_no": "string",
    "department": "string",
    "email": "string"
  },
  {
    "id": number,
    "name": "string",
    "roll_no": "string",
    "department": "string",
    "email": "string"
  }
]
```

### Status Codes
- 200 OK
- 500 Internal Server Error

## Get Student by ID

### Endpoint
    GET /students/{id}

### Route Params
- id : number (Student ID)

### Response
```json
{
  "id": number,
  "name": "string",
  "roll_no": "string",
  "department": "string",
  "email": "string"
}
```

### Status Codes
- 200 OK
- 404 Not Found

## Update Student (Full Update)

### Endpoint
    PUT /students/{id}

### Route Params
- id : number (Student ID)

### Headers
- Content-Type: application/json

### Request
```json
{
  "name": "string",
  "roll_no": "string",
  "department": "string",
  "email": "string"
}
```

### Status Codes
- 204 No Content
- 400 Bad Request
- 404 Not Found

## Update Student (Partial Update)

### Endpoint
    PATCH /students/{id}

### Route Params
- id : number (Student ID)

### Headers
- Content-Type: application/json

### Request
```json
{
  "email": "string"
}
```

### Response
```json
{
  "id": number,
  "name": "string",
  "roll_no": "string",
  "department": "string",
  "email": "string"
}
```

### Status Codes
- 200 OK
- 400 Bad Request
- 404 Not Found

## Delete Student

### Endpoint
    DELETE /students/{id}

### Route Params
- id : number (Student ID)

### Status Codes
- 204 No Content
- 404 Not Found