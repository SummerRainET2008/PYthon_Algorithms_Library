'''
Author: Tian Xia (TianXia0209@gmail.com)
'''

from pyal.list.linked_list import LinkedList


class Queue:
  def __init__(self):
    self._data = LinkedList()

  def push(self, data):
    self._data.push_front(data)

  def pop(self):
    '''
    :return: popped element
    '''
    return self._data.pop_back()

  def __len__(self):
    return self.size()

  def size(self):
    return self._data.size()

  def peek(self):
    return self._data.last_element()
