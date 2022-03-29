import pytest

def setUp():
    print("open amazon app")
    print("user logged in")
    yield
    print("logged out")
    print("closed amazon")

def test_checkout(setUp):
    print("made payment successfully")