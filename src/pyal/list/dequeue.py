'''
Author: Tian Xia (TianXia0209@gmail.com)
'''

from pyal.list.linked_list import LinkedList


class Dequeue:
  def __init__(self):
    self._data = LinkedList()

  def push_front(self, data):
    self._data.push_front(data)

  def push_back(self, data):
    self._data.push_back(data)

  def pop_back(self):
    assert self._data.size() > 0
    return self._data.pop_back()

  def pop_front(self):
    assert self._data.size() > 0
    return self._data.pop_front()

  def size(self):
    return self._data.size()

  def peek_back(self):
    assert self._data.size() > 0
    return self._data.rbegin()()

  def peek_front(self):
    assert self._data.size() > 0
    return self._data.begin()()
