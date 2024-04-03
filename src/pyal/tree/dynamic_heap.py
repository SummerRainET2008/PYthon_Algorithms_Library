'''
Author: Tian Xia (TianXia0209@gmail.com)
'''

import collections


# Min-heap
class DynamicHeap:
  '''
  id: unique.
  value: used to compare in a heap
  '''
  Item = collections.namedtuple("Item", ["id", "value"])

  def __init__(self):
    self._id2pos = {}
    self._data = [self.Item(None, None)]  # [(value, key, ...)]

  def _assign_item(self, pos, item: Item):
    if pos == len(self._data):
      self._data.append(item)
    elif pos < len(self._data):
      self._data[pos] = item
    else:
      assert False

    self._id2pos[item.id] = pos

  def _pop_item(self):
    assert self.size() > 0
    item = self._data.pop()
    del self._id2pos[item.id]

  def __len__(self):
    return self.size()

  def size(self):
    return len(self._data) - 1

  def top(self):
    assert self.size() > 0
    return self._data[1]

  def push(self, id, value):
    if id in self._id2pos:
      self._update(id, value)
      return

    pos = len(self._data)
    self._assign_item(pos, self.Item(id=id, value=value))
    self._adjust_bottom_to_up(pos)
    # print(self.__data)

  def pop(self):
    '''min heap'''
    assert self.size() > 0

    ret = self._data[1]
    if self.size() == 1:
      self._pop_item()
      return ret

    del self._id2pos[ret.id]
    last = self._data.pop()
    self._assign_item(1, last)

    self._adjust_up_to_bottom(1)

    # print(self.__data)
    return ret

  def get(self, id):
    pos = self._id2pos.get(id, -1)
    return None if pos == -1 else self._data[pos].value

  def remove(self, id):
    pos = self._id2pos.get(id, None)
    if pos is None:
      return

    del self._id2pos[id]
    if pos == len(self._data) - 1:
      self._data.pop()
      return

    old_item = self._data[pos]
    new_item = self._data.pop()
    self._assign_item(pos, new_item)
    if new_item.value < old_item.value:
      self._adjust_bottom_to_up(pos)
    else:
      self._adjust_up_to_bottom(pos)

  def _update(self, id, value):
    assert id in self._id2pos

    pos = self._id2pos[id]
    old_item = self._data[pos]
    if value == old_item.value:
      return

    new_item = self.Item(id=old_item.id, value=value)
    self._data[pos] = new_item
    if value < old_item.value:
      self._adjust_bottom_to_up(pos)
    else:
      self._adjust_up_to_bottom(pos)

  def _adjust_bottom_to_up(self, pos):
    f = pos // 2
    if f >= 1 and self._data[f].value > self._data[pos].value:
      item = self._data[pos]
      self._assign_item(pos, self._data[f])
      self._assign_item(f, item)
      self._adjust_bottom_to_up(f)

  def _adjust_up_to_bottom(self, pos):
    cands = [(self._data[s].value, s) for s in [pos * 2, pos * 2 + 1]
             if s < len(self._data)]
    if cands == []:
      return

    s = min(cands)[1]
    if self._data[pos].value < self._data[s].value:
      return

    item = self._data[s]
    self._assign_item(s, self._data[pos])
    self._assign_item(pos, item)

    self._adjust_up_to_bottom(s)


def case_1():
  heap = DynamicHeap()
  heap.push(0, 10)
  heap.push(1, 1)
  heap.push(2, 20)
  heap.push(3, 30)
  heap.push(4, 2)
  heap.push(5, 90)

  heap.push(0, 0)
  heap.push(1, 25)
  heap.push(5, 10)

  heap.remove(4)
  heap.remove(3)

  heap.push(5, 20)
  heap.push(6, 0)
  heap.push(0, 1)

  while heap.size() > 2:
    print(heap.top())
    heap.pop()
  print("-" * 32)

  heap.push(7, 100)
  # heap.remove(5)
  heap.push(1, 15)

  while heap.size() > 0:
    print(heap.top())
    heap.pop()


def main():
  case_1()
  # test_2()


if __name__ == "__main__":
  main()
