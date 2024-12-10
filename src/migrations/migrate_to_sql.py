# src/migrations/migrate_to_sql.py
import sqlite3
import psycopg2

def migrate_data():
    """
    Migrate data from SQLite to PostgreSQL.
    """
    sqlite_conn = sqlite3.connect('funds.db')
    pg_conn = psycopg2.connect("dbname=fund_management user=your_user password=your_password")

    sqlite_cursor = sqlite_conn.cursor()
    pg_cursor = pg_conn.cursor()

    # Fetch all records from SQLite
    sqlite_cursor.execute("SELECT * FROM funds")
    rows = sqlite_cursor.fetchall()

    # Insert data into PostgreSQL
    for row in rows:
        pg_cursor.execute("""
        INSERT INTO funds (id, name, manager, description, nav, creation_date, performance)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, row)

    pg_conn.commit()
    sqlite_conn.close()
    pg_conn.close()
