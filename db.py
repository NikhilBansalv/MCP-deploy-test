"""
Database access layer for the MCP Internship Project.

This module provides helper functions to interact with the
SQLite database, including CRUD operations for users,
products, and orders.
"""

from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent
DB_NAME = BASE_DIR / "database.db"


def get_connection() -> sqlite3.Connection:
    """
    Create and return a connection to the SQLite database.
    """
    return sqlite3.connect(DB_NAME)


# ==========================
# USERS
# ==========================

def list_users():
    """Retrieve all users from the database."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()
    finally:
        conn.close()


def get_user_by_id(user_id: int):
    """Retrieve a user by their ID."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE id = ?",
            (user_id,)
        )
        return cursor.fetchone()
    finally:
        conn.close()


def search_user_by_name(name: str):
    """Search users by name."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE name LIKE ?",
            (f"%{name}%",)
        )
        return cursor.fetchall()
    finally:
        conn.close()


def create_user(name: str, email: str) -> str:
    """Create a new user."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO users(name, email)
            VALUES (?, ?)
            """,
            (name, email)
        )
        conn.commit()
        return "User created successfully."

    except sqlite3.IntegrityError:
        return "A user with this email already exists."

    finally:
        conn.close()


def delete_user(user_id: int) -> str:
    """Delete a user by ID."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM users WHERE id = ?",
            (user_id,)
        )
        conn.commit()

        if cursor.rowcount == 0:
            return "User not found."

        return "User deleted successfully."

    finally:
        conn.close()


# ==========================
# PRODUCTS
# ==========================

def list_products():
    """Retrieve all products."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        return cursor.fetchall()
    finally:
        conn.close()


def get_product_by_id(product_id: int):
    """Retrieve a product by its ID."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM products WHERE id = ?",
            (product_id,)
        )
        return cursor.fetchone()
    finally:
        conn.close()


def search_products(keyword: str):
    """Search products by name."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM products
            WHERE name LIKE ?
            """,
            (f"%{keyword}%",)
        )
        return cursor.fetchall()
    finally:
        conn.close()


# ==========================
# ORDERS
# ==========================

def list_orders():
    """Retrieve all orders with user and product details."""
    conn = get_connection()
    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                orders.id,
                users.name,
                products.name,
                orders.quantity,
                orders.order_date
            FROM orders
            JOIN users
                ON users.id = orders.user_id
            JOIN products
                ON products.id = orders.product_id
        """)

        return cursor.fetchall()
    finally:
        conn.close()