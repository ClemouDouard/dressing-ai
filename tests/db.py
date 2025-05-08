import sqlite3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.db import get_connection, add_user

if __name__ == "__main__":
    conn = get_connection()
    cursor = conn.cursor()
    username = 'test_user'
    add_user(username, 'hashed_password')
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user:
        print("✅ Utilisateur inséré :", user)
    else:
        print("❌ Utilisateur non trouvé dans la base.")