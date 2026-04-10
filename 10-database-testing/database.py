import sqlite3
import os
from datetime import datetime

DB_NAME = "test_users.db"


def get_connection():
    """
    Return sqlite3 connection
    """
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # omogućava dict-like pristup
    return conn


def init_database():
    """
    Create users table
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            age INTEGER,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def create_user(name, email, age):
    """
    Insert user, raise ValueError if email exists
    """
    if not isinstance(name, str) or not name.strip():
        raise ValueError("name is required")
    if not isinstance(email, str) or not email.strip():
        raise ValueError("email is required")
    if age is not None:
        if not isinstance(age, int):
            raise ValueError("age must be int")
        if age < 0:
            raise ValueError("age must be non-negative")

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO users (name, email, age, created_at)
            VALUES (?, ?, ?, ?)
        """, (name, email, age, datetime.utcnow().isoformat()))

        conn.commit()
        return cursor.lastrowid

    except sqlite3.IntegrityError:
        raise ValueError("Email already exists")

    finally:
        conn.close()


def _row_to_dict(row):
    if row is None:
        return None
    return dict(row)


def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()

    conn.close()
    return _row_to_dict(row)


def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    row = cursor.fetchone()

    conn.close()
    return _row_to_dict(row)


def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    conn.close()
    return [dict(row) for row in rows]


def update_user(user_id, name=None, email=None, age=None):
    """
    Update fields, return True if updated, False otherwise
    """
    if name is not None and (not isinstance(name, str) or not name.strip()):
        raise ValueError("name is required")
    if email is not None and (not isinstance(email, str) or not email.strip()):
        raise ValueError("email is required")
    if age is not None:
        if not isinstance(age, int):
            raise ValueError("age must be int")
        if age < 0:
            raise ValueError("age must be non-negative")

    conn = get_connection()
    cursor = conn.cursor()

    fields = []
    values = []

    if name is not None:
        fields.append("name = ?")
        values.append(name)
    if email is not None:
        fields.append("email = ?")
        values.append(email)
    if age is not None:
        fields.append("age = ?")
        values.append(age)

    if not fields:
        conn.close()
        return False

    values.append(user_id)

    try:
        cursor.execute(f"""
            UPDATE users
            SET {', '.join(fields)}
            WHERE id = ?
        """, values)

        conn.commit()
        return cursor.rowcount > 0

    except sqlite3.IntegrityError:
        raise ValueError("Email already exists")

    finally:
        conn.close()


def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

    success = cursor.rowcount > 0
    conn.close()
    return success


def delete_all_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users")
    conn.commit()

    conn.close()
    return True


def drop_database():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
