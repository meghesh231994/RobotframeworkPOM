import pytest


@pytest.fixture()
def test_firstprogram():
    print('first execution')


@pytest.fixture()
def loaddata():
    print('dataload')
    return ['meghesh','bhu']


