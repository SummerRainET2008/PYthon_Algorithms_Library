'''
Author: Tian Xia (TianXia0209@gmail.com)
'''

# from pyal import BinaaryIndexedTree
from .binary_indexed_tree import BinaryIndexedTree

def test_basic():
  bin_tree = BinaryIndexedTree(4)
  bin_tree.update(0, 1)
  bin_tree.update(1, 2)
  bin_tree.update(2, 3)
  bin_tree.update(3, 4)
  # [1, 2, 3, 4]
  assert bin_tree.range_sum(0, 4) == 10

  bin_tree.update(1, 10)
  # [1, 12, 3, 4]
  assert bin_tree.range_sum(0, 4) == 20
  assert bin_tree.range_sum(1, 2) == 12

  bin_tree.update(3, -4)
  assert bin_tree.range_sum(3, 4) == 0
  assert bin_tree.range_sum(0) == 16
  assert bin_tree.range_sum(None, 4) == 16
  assert bin_tree.range_sum(None, None) == 16

def test_inverted_number():
  data = [5, 2, 1, 4, 3, 2, 1, 3, 5, 3, 2, 1]  # 待求逆序数的数组
  #data = [3, 1, 2]
  maxv = max(data)
  assert min(data) >= 0

  bin_tree = BinaryIndexedTree(maxv + 1)
  ret = [None] * len(data)
  for p, d in enumerate(data):
    index = d
    ret[p] = bin_tree.range_sum(index + 1, maxv + 1)
    bin_tree.update(index, 1)

  assert ret == [0, 1, 2, 1, 2, 3, 5, 2, 0, 3, 6, 9]
