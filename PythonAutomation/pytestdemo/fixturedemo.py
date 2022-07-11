import pytest


@pytest.mark.usefixtures('test_firstprogram')
class Testdemo:

    def test_fixturedemo(self):
        print('I will execute')

    def test_fixturedemo1(self):
        print('I will execute 1')

    def test_fixturedemo2(self):
        print('I will execute 2')

    def test_fixturedemo3(self):
        print('I will execute 3')