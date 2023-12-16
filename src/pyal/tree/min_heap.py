'''
Author: Tian Xia (TianXia0209@gmail.com)
'''

import heapq


class MinHeap:
  def __init__(self):
    self._data = []

  def __len__(self):
    return self.size()

  def size(self):
    return len(self._data)

  def top(self):
    assert self.size() > 0
    return self._data[0]

  def push(self, value):
    heapq.heappush(self._data, value)

  def pop(self):
    '''min heap'''
    assert self.size() > 0
    return heapq.heappop(self._data)
