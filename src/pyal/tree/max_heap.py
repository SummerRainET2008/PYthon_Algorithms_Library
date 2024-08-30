'''
Author: Tian Xia (TianXia0209@gmail.com)
'''

import heapq

class _Pair:
  def __init__(self, user_value):
    self.value = user_value

  def __lt__(self, other):
    return not (self.value < other.value)

class MaxHeap:
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
    heapq.heappush(self._data, _Pair(value))

  def pop(self):
    '''min heap'''
    assert self.size() > 0
    return heapq.heappop(self._data).value
