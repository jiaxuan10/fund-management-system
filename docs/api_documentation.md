# API Documentation

## Overview

This API is designed to manage investment funds. It provides endpoints to retrieve, create, update, and delete funds, as well as update fund performance.

## Endpoints

### GET /funds
Retrieve a list of all funds.

**Response**:
- 200 OK: Returns a list of all funds in JSON format.
- Example:
    ```json
    [
        {
            "id": 1,
            "name": "Global Fund",
            "manager": "John Doe",
            "nav": 1000.0,
            "performance": 5.5
        }
    ]
    ```

### POST /funds
Create a new fund.

**Request**:
- Required fields: `name`, `manager`, `nav`.
- Optional fields: `description`, `performance`.

**Response**:
- 201 Created: Returns the details of the created fund.

### GET /funds/{id}
Retrieve details of a specific fund by its ID.

**Response**:
- 200 OK: Returns the fund's details.
- 404 Not Found: If the fund with the given ID does not exist.

### PUT /funds/{id}/performance
Update the performance of a specific fund.

**Request**:
- Required field: `performance`.

**Response**:
- 200 OK: Returns the updated fund with the new performance.

### DELETE /funds/{id}
Delete a specific fund by its ID.

**Response**:
- 204 No Content: The fund has been successfully deleted.
- 404 Not Found: If the fund with the given ID does not exist.

## Sample Requests

### GET /funds
```bash
curl -X GET http://127.0.0.1:5000/funds
