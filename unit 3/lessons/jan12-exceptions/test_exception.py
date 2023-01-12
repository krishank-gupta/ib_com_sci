from exception import division
import pytest

def test_valid():
    assert division(10,2) == 5
    assert division(5,2) == 2.5

def test_invalid():
    with pytest.raises(ValueError):
        division(5,0)
    with pytest.raises(TypeError):
        division("Foo", "Bar")

        