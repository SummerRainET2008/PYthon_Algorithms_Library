'''
Author: Tian Xia (TianXia0209@gmail.com)
'''
import pyal


def test_basic():
  disjoint_set = pyal.DisjointSet(10)
  assert disjoint_set.get_cluster_id(0) == 0
  assert disjoint_set.get_cluster_id(1) == 1
  assert disjoint_set.get_cluster_num() == 10

  disjoint_set.combine(0, 1)
  assert disjoint_set.get_cluster_num() == 9
  assert disjoint_set.get_cluster_id(0) == disjoint_set.get_cluster_id(1)
