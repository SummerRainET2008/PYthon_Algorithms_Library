'''
>> nosetests -v --nocapture test/tree_map_TEST.py
'''

from .algorithm import *

def test_read_file():
  file_name = "/tmp/.test.txt"
  with open(file_name, "w") as fout:
    print("Hello World", file=fout)

  assert read_file_content(file_name)  == "Hello World"
  assert list(read_file_lines(file_name))[0] == "Hello World"

def test_thread_pool():
  def f(m: int, n: int):
    return m + n

  pool = Pool(4)
  result = 0
  for r in pool.map1(f, ((m, m + m) for m in range(10))):
    result += r
    print(r, result)

  assert result == 135


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
  data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3]
  data1 = unique(data)
  assert data1 == [1, 2, 3]

  end = unique_in_place(data)
  assert data[: end] == [1, 2, 3]


def test_argmax():
  data = [1, 2, 3, 4, 5, 6, 7]
  assert data[argmax(data)] == 7
  assert data[argmin(data)] == 1


def test_make_list():
  data = make_list((2, 3, 4), None)
  assert len(data) == 2 and len(data[0]) == 3 and len(data[0][0]) == 4

  data = make_list((3,), [])
  data[0].append(1)
  data[1].append(2)
  assert data[0] == [1]
  assert data[2] == []

def test_the_kth_element():
  import random
  data = [1, 2, 3, 4, 5, 6]
  random.shuffle(data)

  kth_smallest_element(data, 0)
  assert data[0] == 1

  kth_smallest_element(data, 1)
  assert data[1] == 2

  kth_smallest_element(data, 2)
  assert data[2] == 3

  kth_smallest_element(data, 3)
  assert data[3] == 4

  data = [1, 2, 3, 4, 5, 6]
  for _ in range(factorial(len(data))):
    data = next_permutation(data)

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


def test_discrete_sample():
  from collections import Counter
  probs = [0.1, 0.2, 0.7]
  sampled_poses = [discrete_sample(probs) for _ in range(10000)]
  dist = Counter(sampled_poses)
  freq_ratio = dist[2] / dist[0]
  print(freq_ratio)
  assert freq_ratio > 6


def test_top_k():
  import random
  data = [1, 2, 3, 4, 5, 6]
  random.shuffle(data)

  ans = top_n(data, 3, type="min", to_sort=True)
  assert ans == [1, 2, 3]

  ans = top_n(data, 3, type="max", to_sort=True)
  assert ans == [6, 5, 4]


def test_find_if():
  data = [1, 2, 3, 4, 5, 6]

  assert data[find_first_if(data, lambda d: d % 2 == 0)] == 2
  assert data[find_last_if(data, lambda d: d % 2 == 0)] == 6


def test_combination_with_duplicate():
  data = [1, 1, 1, 2, 2, 2, 3, 3, 4]
  combs = list(combinations_with_duplicate(data, 3))
  assert len(combs) == 15
  print(combs)

  data = [1, 1, 2, 2]
  combs = list(combinations_with_duplicate(data, 2))
  assert len(combs) == 3


def test_group_data():
  import random

  data = [1, 1, 2, 2, 0, 0, 0]
  groups = list(group_data(data, sequential=True))
  assert groups == [(1, 2), (2, 2), (0, 3)]

  random.shuffle(data)
  groups = list(group_data(data, sequential=False))
  groups = sorted(groups)
  assert groups == [(0, 3), (1, 2), (2, 2)]

def test_binary_search():  
  def find(sorted_data: list, target):
    size = len(sorted_data)
    pos = binary_search(sorted_data, 0, size, lambda x: x < target)
    if pos < size and sorted_data[pos] == target:
      return pos 
    return size 

  def lower_bound(sorted_data: list, target):
    size = len(sorted_data)
    pos = binary_search(sorted_data, 0, size, lambda x: x < target)
    return pos

  def upper_bound(sorted_data: list, target):
    size = len(sorted_data)
    pos = binary_search(sorted_data, 0, size, lambda x: x <= target)
    return pos

  def test():
    import random

    data = sorted([random.randrange(10, 100) for _ in range(1000)])
    targets = [random.randrange(0, 150) for _ in range(1000)]

    for target in targets:
      pos = find(data, target)
      if pos == len(data):
        assert target not in data
      else:    
        assert target in data

      pos = lower_bound(data, target)
      for index, d in enumerate(data):
        if target <= d:
          assert pos <= index
          break

      pos = upper_bound(data, target)
      for index, d in enumerate(data):
        if target < d:
          assert pos <= index
          break

  test()

