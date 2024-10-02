from _2createWorld import createWorld
import pytest


def test_createWorld():
    #ssert createWorld== True
    assert createWorld(true) == True
    print(createWorld == True)
    
pytest.main(["-v", "--tb=line", "-rN", __file__])    