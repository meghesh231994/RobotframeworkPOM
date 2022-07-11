import pytest


@pytest.mark.usefixtures('loaddata')
class TestEx():
        def test_edit(self,loaddata):
            print(loaddata[1])
