import pytest

@pytest.fixture(scope="session",autouse=True)
def setUp():
    print("open amazon app")
    print("user logged in")
    yield
    print("user logged out")
    print("close amazon app")