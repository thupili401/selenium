import pytest


@pytest.fixture(autouse=True)
def setup():
    print("Launch the brouser")
    print("Launch the application")
    yield
    print("Close the application")
    print("close the browser")
