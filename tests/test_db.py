from db import *

def test_list_users():
    users = list_users()
    assert len(users) > 0


def test_get_user():
    user = get_user_by_id(1)
    assert user is not None


def test_invalid_user():
    user = get_user_by_id(9999)
    assert user is None


def test_search_user():
    users = search_user_by_name("Nik")
    assert len(users) > 0


def test_products():
    products = list_products()
    assert len(products) > 0


def test_orders():
    orders = list_orders()
    assert len(orders) > 0