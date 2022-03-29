import pytest

@pytest.fixture()
def setUp():
    print("user login")
    yield
    print("user logout")


def test_AddItemtocart(setUp):
    print("added successfully")


def test_RemoveItemfromCart(setUp):
    print("removed successfully")
