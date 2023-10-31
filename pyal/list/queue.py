'''
Author: Tian Xia (TianXia0209@gmail.com)
'''

from .linked_list import LinkedList

class Queue:
  def __init__(self):
    self._data = LinkedList()

  def push(self, data):
    self._data.push_front(data)

  def pop(self):
    assert self._data.size() > 0
    return self._data.pop_back()

  def size(self):
    return self._data.size()

  def peek(self):
    assert self._data.size() > 0
    return self._data.rbegin()()
