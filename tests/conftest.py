import pytest


@pytest.fixture()
def test_set_login_and_logout():
    print("open Url")
    print("login")
    yield
    print("logout")
    print("close")