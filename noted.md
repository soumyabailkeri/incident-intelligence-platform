# Incident Intelligence Platform - Learning Notes

## Day 1 - Project Setup and DRF Fundamentals

### Project Creation

Created Django project:

```bash
django-admin startproject incident_platform
```

Created app:

```bash
python manage.py startapp incdnt
```

Registered app in INSTALLED_APPS.

---

## Django Architecture Mapping

### My Current Product Development Experience

| Current Product Platform | Django Equivalent    |
| ------------------------ | -------------------- |
| Domain                   | Model                |
| Query File               | ORM Query            |
| Controller               | View                 |
| I/O Class                | Serializer           |
| Generate Code            | Migration            |
| Service Config           | settings.py          |
| Intermodule JSON         | API Request/Response |
| Workspace Operation      | API Endpoint         |
| Access Control           | Permissions          |

---

## Models Implemented

### Category

Stores incident categories.

Examples:

* Payments
* Authentication
* Infrastructure

---

### UserProfile

Extends Django User.

Stores:

* Department
* Phone Number
* Role

Relationship:

User -> OneToOne -> UserProfile

---

### Incident

Stores:

* Title
* Description
* Category
* Priority
* Status
* Reported By
* Assigned To
* Closed By
* Resolution Summary
* Audit Timestamps

---

## Business Rules Learned

### Foreign Key

One object references another object.

Example:

Incident -> Category

Many incidents can belong to one category.

---

### One To One

One user has exactly one profile.

User -> UserProfile

---

### on_delete

Determines behavior when parent object is deleted.

Examples:

CASCADE
PROTECT
SET_NULL

---

## Migrations

Equivalent to generated SQL scripts in my current platform.

### Commands

Generate migration:

```bash
python manage.py makemigrations
```

Apply migration:

```bash
python manage.py migrate
```

Understanding:

makemigrations = prepare changes

migrate = execute changes

---

## ORM

Object Relational Mapping.

Example:

```python
Incident.objects.get(id=1)
```

Django converts ORM code into SQL automatically.

---

## Serializer

Purpose:

Python Object -> JSON

JSON -> Python Object

Similar to API request/response mapping.

---

## API Development

Created:

GET /api/incidents/

Returns list of incidents.

Implemented serializer customization:

category_name
reported_by_username

instead of only numeric IDs.

---

## JWT Authentication

Installed:

djangorestframework-simplejwt

Created endpoint:

POST /api/token/

Request:

{
"username": "user",
"password": "password"
}

Response:

{
"refresh": "...",
"access": "..."
}

---

## Authentication vs Authorization

Authentication

Question:

Who are you?

Example:

JWT Token Validation

Result:

request.user

---

Authorization

Question:

What are you allowed to do?

Examples:

Admin
Manager
Developer

Different permissions for different actions.

---

## HTTP Status Codes Learned

200 OK

Request successful.

---

401 Unauthorized

Authentication missing or invalid.

Example:

No JWT token provided.

---

403 Forbidden

User authenticated.

But not allowed to perform operation.

---

404 Not Found

Requested object does not exist.

Example:

Incident ID 999

Response:

No Incident matches the given query.

---

## API Testing

Installed Postman.

Successfully:

* Generated JWT Token
* Added Bearer Token
* Called protected endpoint

Request Header:

Authorization: Bearer <access_token>

---

## Key Realization

Enterprise architecture concepts remain similar across technologies.

Current Product Platform Concepts translate directly into Django/DRF concepts.

Main learning focus is implementation, not architecture.
