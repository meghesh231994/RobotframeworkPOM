import pytest


def test_gee(test_firstprogram):
    print('second')

@pytest.mark.skip
def test_he():
    msg = 'hiii'
    assert msg == 'hello'
