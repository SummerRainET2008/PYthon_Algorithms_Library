'''
>> nosetests -v --nocapture test/tree_map_TEST.py
'''
from pyal.common.algorithm import *

def test_lower_bound():
  data = [0, 1, 1, 1, 2, 3, 4, 5]
  pos = lower_bound(data, 1)
  assert data[pos] == 1

  pos = upper_bound(data, 1)
  assert data[pos] == 2

def test_rotate():
  data = [0, 1, 2, 3, 4, 5, 6, 7]

  data1 = rotate(data, 0)
  assert data1 == data

  data1 = rotate(data, 2, 1, None)
  assert data1 == [0, 2, 3, 4, 5, 6, 7, 1]

def test_is_sorted():
  data = [1, 1, 1, 2, 2, 3]
  assert is_sorted(data, False)
  assert not is_sorted(data, True)

def test_unique():
  data = [1, 1, 1, 2, 2, 3]
  data = unique(data)
  assert data == [1, 2, 3]

def test_top_k():
  import random
  data = [1, 2, 3, 4, 5, 6, 7]
  random.shuffle(data)
  assert top_k(data, 3, "max", to_sort=True) == [7, 6, 5]
  assert top_k(data, 3, "min", to_sort=True) == [1, 2, 3]

def test_argmax():
  data = [1, 2, 3, 4, 5, 6, 7]
  assert data[argmax(data)] == 7
  assert data[argmin(data)] == 1
