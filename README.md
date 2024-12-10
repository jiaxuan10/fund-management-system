## Overview

Task Breakdown
Task 1: Data Model Design
File: src/models.py
Description: Create an InvestmentFund class using SQLAlchemy to represent funds.
Task 2: REST API Development
File: src/routes.py
Description: Implement API endpoints to manage funds.
Task 3: Data Persistence
File: src/database.py
Description: Implement SQLite database for storing fund data.
Task 4: SQL Database Schema
File: src/migrations/schema.sql
Description: Define the database schema for funds.
Task 5: SQL Data Migration
File: src/migrations/migrate_to_sql.py
Description: Migrate data from SQLite to PostgreSQL.
Task 6: Error Handling
File: src/app.py
Description: Implement error handling for common API errors (e.g., 404, 400).
Task 7: Testing
Files: tests/test_api.py, tests/test_sql.py
Description: Write test cases to verify the API and database functionality.
Task 8: Documentation
Files: docs/api_documentation.md, docs/database_documentation.md
Description: Provide documentation for API endpoints and the database schema.# Fund Management System API

A RESTful API built with **Flask** and **SQLAlchemy** to manage investment funds. Allows CRUD operations (Create, Read, Update, Delete) on funds and updates to fund performance metrics.

## Setup

### Prerequisites

- Python 3.x
- pip

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/fund-management-system.git
   cd fund-management-system

   ```

2. **Create a virtual environment**:
   python -m venv venv
   source venv/bin/activate # macOS/Linux
   .\venv\Scripts\activate # Windows

3. **Install dependencies**:
   pip install -r requirements.txt

4. **Run the application**:
   python -m src.app
