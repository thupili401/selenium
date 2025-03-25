import pytest


@pytest.mark.skip
def test_asser_tion():
    print("1st function")

@pytest.mark.regression
def test_asser_tion_1():
    print("2nd function")

@pytest.mark.regression
def test_asser_tion_1():
    print("3nd function")

@pytest.mark.smoke
def test_asser_tion_1():
    print("4nd function")


