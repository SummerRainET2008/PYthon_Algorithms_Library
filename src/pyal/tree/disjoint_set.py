'''
Author: Tian Xia (TianXia0209@gmail.com)
'''

class DisjointSet:
  def __init__(self):
    self._fathers = {}
    self._sizes = {}

  def combine(self, a, b)-> bool:
    c1 = self.get_cluster_id(a)
    c2 = self.get_cluster_id(b)
    if c1 == c2:
      return False

    if self._sizes.get(c1, 1) > self._sizes.get(c2, 1):
      return self.combine(b, a)

    self._fathers[c1] = c2
    self._sizes[c2] = self._sizes.get(c2, 1) + self._sizes.get(c1, 1)
    return True

  def get_cluster_id(self, a):
    father = self._fathers.get(a, None)
    if father is None:
      return a
    cluster_id = self.get_cluster_id(father)
    self._fathers[a] = cluster_id

    return cluster_id
