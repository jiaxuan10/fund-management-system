# Database Documentation

## Schema

The database consists of a single table, `funds`, which has the following columns:

- **id**: A unique identifier for the fund (primary key, auto-increment).
- **name**: The name of the fund (non-nullable).
- **manager**: The manager of the fund (non-nullable).
- **description**: A description of the fund (nullable).
- **nav**: The Net Asset Value of the fund (non-nullable).
- **creation_date**: The date the fund was created (default: current timestamp).
- **performance**: The performance of the fund (nullable).

## SQL Schema

```sql
CREATE TABLE funds (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    manager VARCHAR(255) NOT NULL,
    description TEXT,
    nav FLOAT NOT NULL,
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    performance FLOAT
);
