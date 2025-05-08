import sqlite3

def get_connection():
    conn = sqlite3.connect('data/db.sqlite')
    return conn

def add_user(username: str, password_hash: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO users (username, password_hash)
        VALUES (?, ?)
    ''', (username, password_hash))

    conn.commit()
    conn.close()

