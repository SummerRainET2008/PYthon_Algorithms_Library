'''
Author: Tian Xia (TianXia0209@gmail.com)
'''

import collections
from .linked_list import ListNode, LinkedList

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


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
  cache = LRUCache(2)
  for item in [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]:
    print("input:", item)
    if len(item) == 1:
      print("get:", cache.get(item[0]))
    elif len(item) == 2:
      cache.put(item[0], item[1])
    # cache.linked_list.display()
