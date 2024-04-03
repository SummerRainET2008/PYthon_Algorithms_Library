'''
Author: Tian Xia (TianXia0209@gmail.com)
'''

from pyal import DynamicHeap


def test_basic():
  heap = DynamicHeap()
  for value in reversed(range(10)):
    heap.push(id=value, value=value)
    assert heap.top().id == value


def test_update():
  heap = DynamicHeap()
  heap.push(1, 5)
  heap.push(2, 6)
  heap.push(3, 7)
  heap.push(4, 8)
  heap.push(5, 9)

  assert heap.top() == DynamicHeap.Item(1, 5)

  heap.push(5, 4)
  assert heap.top() == DynamicHeap.Item(5, 4)

  heap.remove(5)
  heap.remove(1)
  assert heap.top() == DynamicHeap.Item(2, 6)

  heap.pop()
  assert heap.top() == DynamicHeap.Item(3, 7)
  heap.pop()

  assert heap.get(4) == 8
  assert heap.top() == DynamicHeap.Item(4, 8)
