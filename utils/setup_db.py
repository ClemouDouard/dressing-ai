import sqlite3

from database.db import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    #Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password_hash TEXT NOT NULL
        )    
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()