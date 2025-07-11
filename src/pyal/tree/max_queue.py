'''
Author: Tian Xia (TianXia0209@gmail.com)
'''

from collections import deque

class MaxQueue:
  def __init__(self):
    self._data_queue = deque()
    self._maxv_queue = deque()

  def max(self):
    return self._maxv_queue[0]

  def push(self, d):
    self._data_queue.append(d)
    while len(self._maxv_queue) > 0 and not (self._maxv_queue[-1] >= d):
      self._maxv_queue.pop()
    self._maxv_queue.append(d)

  def pop(self):
    v = self._data_queue.popleft()
    if v == self._maxv_queue[0]:
      self._maxv_queue.popleft()
    return v

  def size(self):
    return len(self._data_queue)

  def __len__(self):
    return self.size()
