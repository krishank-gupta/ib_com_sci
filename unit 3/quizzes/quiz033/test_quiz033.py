import pytest
from quiz033 import mystery

def test_empty_lists():
  assert mystery([], []) == []

def test_one_common_element():
  assert mystery([1, 2, 3], [3, 4, 5]) == [3]

def test_multiple_common_elements():
  assert mystery([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

# import inc_dec    # The code to test
# import pytest 

# def test_increment():
#     assert inc_dec.increment(3) == 4

# def test_decrement():
#     assert inc_dec.decrement(3) == 4
