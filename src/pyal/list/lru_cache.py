'''
Author: Tian Xia (TianXia0209@gmail.com)
'''

import collections
from pyal.list.linked_list import LinkedList


class Item(collections.namedtuple("Item", ["key", "value"])):
  def update(self, value):
    return self._replace(value=value)


class LRUCache:
  def __init__(self, capacity: int):
    self._list = LinkedList()
    self._key2node = {}
    self._capacity = capacity

  def get(self, key: int) -> int:
    node = self._key2node.get(key, None)
    if node is None:
      return -1

    self._update_node(node)
    return node().value

  def put(self, key: int, value: int) -> None:
    node = self._key2node.get(key, None)
    if node is not None:
      node.content = node().update(value)
      self._update_node(node)

    else:
      if len(self._key2node) == self._capacity:
        del self._key2node[self._list.pop_back().key]

      self._list.push_front(Item(key, value))
      self._key2node[key] = self._list.begin()

  def _update_node(self, node):
    if node is not self._list.begin():
      self._list.remove(node)
      self._list.insert(self._list.begin(), node)
