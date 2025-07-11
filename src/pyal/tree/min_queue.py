'''
Author: Tian Xia (TianXia0209@gmail.com)
'''

from collections import deque

class MinQueue:
  def __init__(self):
    self._data_queue = deque()
    self._minv_queue = deque()

  def min(self):
    return self._minv_queue[0]

  def push(self, d):
    self._data_queue.append(d)
    while len(self._minv_queue) > 0 and not (self._minv_queue[-1] <= d):
      self._minv_queue.pop()
    self._minv_queue.append(d)

  def pop(self):
    v = self._data_queue.popleft()
    if v == self._minv_queue[0]:
      self._minv_queue.popleft()
    return v

  def size(self):
    return len(self._data_queue)

  def __len__(self):
    return self.size()
