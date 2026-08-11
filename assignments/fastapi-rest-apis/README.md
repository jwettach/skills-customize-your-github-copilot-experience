# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI to practice route creation, request validation, JSON responses, and basic error handling.

## 📝 Tasks

### 🛠️ Build Core API Endpoints

#### Description

Create a FastAPI application that manages a simple item resource collection with standard REST operations.

#### Requirements

Completed program should:

- Define endpoints for `GET /items`, `GET /items/{item_id}`, `POST /items`, `PUT /items/{item_id}`, and `DELETE /items/{item_id}`
- Use Pydantic models for request and response validation
- Store items in an in-memory list or dictionary
- Return JSON responses with appropriate HTTP status codes
- Include clear success messages for create, update, and delete operations

### 🛠️ Add Validation and Error Handling

#### Description

Enhance the API by validating incoming data and returning helpful error responses when requests are invalid.

#### Requirements

Completed program should:

- Validate required fields for `POST` and `PUT` requests
- Return `404 Not Found` when an item ID does not exist
- Use FastAPI validation to return `422 Unprocessable Entity` for invalid payloads
- Provide descriptive error messages in the response body
