from db import *

def test_create_delete_user():

    create_user(
        "pytest",
        "pytest@gmail.com"
    )

    users = search_user_by_name("pytest")

    assert len(users) == 1

    delete_user(users[0][0])


def test_delete_invalid():

    result = delete_user(99999)

    assert result == "User not found."


def test_product_search():

    result = search_products("Laptop")

    assert len(result) > 0


def test_invalid_product():

    product = get_product_by_id(999)

    assert product is None