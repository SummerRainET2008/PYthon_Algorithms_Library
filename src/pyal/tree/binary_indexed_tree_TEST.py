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
