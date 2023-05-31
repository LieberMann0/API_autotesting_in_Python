import pytest


@pytest.fixture()
def good():
    return 'колбаса'


@pytest.fixture()
def bad():
    return 'калбаса'
