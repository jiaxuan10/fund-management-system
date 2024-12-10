CREATE TABLE funds (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    manager VARCHAR(255) NOT NULL,
    description TEXT,
    nav FLOAT NOT NULL,
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    performance FLOAT
);
