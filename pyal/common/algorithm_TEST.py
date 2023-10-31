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

def test_make_new_list():
  data = make_new_list((2, 3, 4), None)
  assert len(data) == 2 and len(data[0]) == 3 and len(data[0][0]) == 4

def test_the_kth_element():
  import random
  data = [1, 2, 3, 4, 5, 6]
  random.shuffle(data)

  the_kth_element(data, 0)
  assert data[0] == 1

  the_kth_element(data, 1)
  assert data[1] == 2

  the_kth_element(data, 2)
  assert data[2] == 3

  the_kth_element(data, 3)
  assert data[3] == 4

  for _ in range(factorial(len(data))):
    data = next_permutation(data)
    # print(data)

  assert data == [1, 2, 3, 4, 5, 6]

def test_next_permutation():
  data = [1, 2, 3, 4, 5, 6]

  data1 = next_permutation(data)
  assert data1 == [1, 2, 3, 4, 6, 5]

  data2 = next_permutation(data1)
  assert data2 == [1, 2, 3, 5, 4, 6]

def test_combination_permutation():
  assert combinatorial_number(5, 0) == 1
  assert combinatorial_number(5, 1) == 5
  assert combinatorial_number(5, 2) == 10
  assert combinatorial_number(5, 3) == 10
  assert combinatorial_number(5, 4) == 5
  assert combinatorial_number(5, 5) == 1

  assert permutation_number(5, 1) == 5
  assert permutation_number(5, 2) == 20
  assert permutation_number(5, 3) == 60
  assert permutation_number(5, 4) == 120
  assert permutation_number(5, 5) == 120
