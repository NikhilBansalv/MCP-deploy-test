import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Drop tables if they already exist
cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("DROP TABLE IF EXISTS users")

# -------------------------
# USERS TABLE
# -------------------------

cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")

# -------------------------
# PRODUCTS TABLE
# -------------------------

cursor.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL
)
""")

# -------------------------
# ORDERS TABLE
# -------------------------

cursor.execute("""
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    order_date TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(product_id) REFERENCES products(id)
)
""")

# -------------------------
# INSERT USERS
# -------------------------

users = [
    ("Nikhil", "nikhil@gmail.com"),
    ("Rahul", "rahul@gmail.com"),
    ("Ananya", "ananya@gmail.com"),
    ("Priya", "priya@gmail.com"),
    ("Karan", "karan@gmail.com"),
    ("Riya", "riya@gmail.com"),
    ("Aman", "aman@gmail.com"),
    ("Sneha", "sneha@gmail.com"),
    ("Arjun", "arjun@gmail.com"),
    ("Meera", "meera@gmail.com"),
    ("Rohit", "rohit@gmail.com"),
    ("Simran", "simran@gmail.com"),
    ("Aditya", "aditya@gmail.com"),
    ("Neha", "neha@gmail.com"),
    ("Varun", "varun@gmail.com"),
    ("Pooja", "pooja@gmail.com"),
    ("Akash", "akash@gmail.com"),
    ("Ishita", "ishita@gmail.com"),
    ("Yash", "yash@gmail.com"),
    ("Kavya", "kavya@gmail.com")
]

cursor.executemany(
    "INSERT INTO users(name,email) VALUES (?,?)",
    users
)

# -------------------------
# INSERT PRODUCTS
# -------------------------

products = [
    ("Laptop", "Electronics", 75000, 12),
    ("Phone", "Electronics", 35000, 20),
    ("Monitor", "Electronics", 15000, 10),
    ("Keyboard", "Accessories", 2500, 30),
    ("Mouse", "Accessories", 1200, 40),
    ("Headphones", "Accessories", 3500, 25),
    ("Smart Watch", "Wearables", 9000, 15),
    ("Tablet", "Electronics", 28000, 8),
    ("Printer", "Office", 12000, 5),
    ("Router", "Networking", 3000, 18),
    ("SSD", "Storage", 7000, 22),
    ("Hard Disk", "Storage", 5500, 14),
    ("Webcam", "Accessories", 2500, 16),
    ("Microphone", "Accessories", 4200, 9),
    ("USB Drive", "Storage", 800, 50),
    ("Power Bank", "Accessories", 1800, 24),
    ("Gaming Chair", "Furniture", 16000, 7),
    ("Desk Lamp", "Furniture", 1500, 28),
    ("Speaker", "Audio", 5000, 11),
    ("Projector", "Electronics", 45000, 4)
]

cursor.executemany(
    """
    INSERT INTO products(name,category,price,stock)
    VALUES (?,?,?,?)
    """,
    products
)

# -------------------------
# INSERT ORDERS
# -------------------------

orders = []

for _ in range(20):
    user_id = random.randint(1, 20)
    product_id = random.randint(1, 20)
    quantity = random.randint(1, 5)

    random_days = random.randint(0, 30)
    order_date = (
        datetime.now() - timedelta(days=random_days)
    ).strftime("%Y-%m-%d")

    orders.append(
        (
            user_id,
            product_id,
            quantity,
            order_date
        )
    )

cursor.executemany(
    """
    INSERT INTO orders(user_id,product_id,quantity,order_date)
    VALUES (?,?,?,?)
    """,
    orders
)

conn.commit()
conn.close()

print("Database seeded successfully!")