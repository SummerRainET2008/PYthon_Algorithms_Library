'''
Author: Tian Xia (TianXia0209@gmail.com)
'''


class DisjointSet:
  def __init__(self, n):
    self._fathers = {}
    self._sizes = {}
    self._clusters_num = n

  def combine(self, a, b):
    assert 0 <= a < self._clusters_num
    assert 0 <= b < self._clusters_num

    c1 = self.get_cluster_id(a)
    c2 = self.get_cluster_id(b)
    if c1 == c2:
      return

    if self._sizes.get(c1, 1) > self._sizes.get(c2, 1):
      self.combine(b, a)
      return

    self._fathers[c1] = c2
    self._sizes[c2] = self._sizes.get(c2, 1) + self._sizes.get(c1, 1)
    self._clusters_num -= 1

  def get_cluster_id(self, a):
    assert 0 <= a < self._clusters_num

    father = self._fathers.get(a, -1)
    if father == -1:
      return a
    cluster_id = self.get_cluster_id(father)
    self._fathers[a] = cluster_id
    return cluster_id

  def get_cluster_num(self):
    return self._clusters_num
