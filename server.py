"""
MCP Server for the Internship Project.

This server exposes database operations as MCP tools using
the FastMCP framework. It provides tools for managing users,
products, and orders stored in a SQLite database.
"""

import logging
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from db import (
    list_users,
    get_user_by_id,
    search_user_by_name,
    create_user,
    delete_user,
    list_products,
    get_product_by_id,
    search_products,
    list_orders,
)

# Logging Configuration

LOG_DIR = Path(__file__).resolve().parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "server.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# MCP Server

mcp = FastMCP("InternProject")

# Helper Functions

def user_to_dict(user):
    """Convert a user tuple into a dictionary."""
    return {
        "id": user[0],
        "name": user[1],
        "email": user[2],
    }


def product_to_dict(product):
    """Convert a product tuple into a dictionary."""
    return {
        "id": product[0],
        "name": product[1],
        "category": product[2],
        "price": product[3],
        "stock": product[4],
    }


def order_to_dict(order):
    """Convert an order tuple into a dictionary."""
    return {
        "order_id": order[0],
        "user": order[1],
        "product": order[2],
        "quantity": order[3],
        "date": order[4],
    }

# USER TOOLS

@mcp.tool()
def get_all_users():
    """
    Retrieve all users from the database.
    """
    logger.info("Fetching all users")

    users = list_users()

    return [user_to_dict(user) for user in users]


@mcp.tool()
def get_user(user_id: int):
    """
    Retrieve a user by ID.
    """
    logger.info("Fetching user with ID: %s", user_id)

    user = get_user_by_id(user_id)

    if not user:
        return {"message": "User not found"}

    return user_to_dict(user)


@mcp.tool()
def search_user(name: str):
    """
    Search users by name.
    """
    logger.info("Searching user: %s", name)

    users = search_user_by_name(name)

    if not users:
        return {"message": "No users found"}

    return [user_to_dict(user) for user in users]


@mcp.tool()
def add_user(name: str, email: str):
    """
    Create a new user.
    """
    logger.info("Creating user: %s", name)

    return {
        "message": create_user(name, email)
    }


@mcp.tool()
def remove_user(user_id: int):
    """
    Delete a user by ID.
    """
    logger.info("Deleting user with ID: %s", user_id)

    return {
        "message": delete_user(user_id)
    }

# PRODUCT TOOLS

@mcp.tool()
def get_all_products():
    """
    Retrieve all products from the database.
    """
    logger.info("Fetching all products")

    products = list_products()

    return [product_to_dict(product) for product in products]


@mcp.tool()
def get_product(product_id: int):
    """
    Retrieve a product by ID.
    """
    logger.info("Fetching product with ID: %s", product_id)

    product = get_product_by_id(product_id)

    if not product:
        return {"message": "Product not found"}

    return product_to_dict(product)


@mcp.tool()
def search_product(keyword: str):
    """
    Search products using a keyword.
    """
    logger.info("Searching product: %s", keyword)

    products = search_products(keyword)

    if not products:
        return {"message": "No products found"}

    return [product_to_dict(product) for product in products]

# ORDER TOOLS

@mcp.tool()
def get_all_orders():
    """
    Retrieve all orders from the database.
    """
    logger.info("Fetching all orders")

    orders = list_orders()

    return [order_to_dict(order) for order in orders]

# Start MCP Server

if __name__ == "__main__":
    logger.info("Starting MCP Server...")
    mcp.run()