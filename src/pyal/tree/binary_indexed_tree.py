'''
Author: Tian Xia (TianXia0209@gmail.com)

Core idea:
n=11 (b1011)
b1000: storing 1-8  (from b001 - b1000)
b1001: storing 9
b1010: storing 9-10 (b1001, b1010)
b1011: storing 11 (b1011)
b1100: store (b1001, b1010, b1011, b1100)
To summarey, a node with index m, stores numbers from [m - lowest_bit(m) + 1, m].
'''

class _BinaryIndexedTree:
  def __init__(self, max_index):
    self._tree = [0] * (max_index + 1)
    self._max_index = max_index

  def update(self, index: int, delta):
    assert 1 <= index <= self._max_index
    while index <= self._max_index:
      # print(f"update traverse: {true_index=}")
      self._tree[index] += delta
      index += self._lowbit(index)

  def _lowbit(self, index):
    return index & (-index)

  def _get_father(self, index):
    return index - index & (-index)

  def _range_sum(self, index):
    assert 1 <= index <= self._max_index

    ans = 0
    while index > 0:
      ans += self._tree[index]
      index -= self._lowbit(index)

    return ans

  def range_sum(self, begin, end):
    assert 1 <= begin < end <= len(self._tree)

    if begin == 1:
      return self._range_sum(end - 1)

    return self._range_sum(end - 1) - self._range_sum(begin - 1)

class BinaryIndexedTree:
  def __init__(self, size):
    self._tree = _BinaryIndexedTree(size)
    self._size = size

  def update(self, index: int, delta):
    self._tree.update(index + 1, delta)

  def range_sum(self, begin, end=None):
    if begin is None:
      begin = 0
    if end is None:
      end = self._size
    if not (end - begin > 0):
      return 0
    if not 0 <= begin < self._size:
      return 0


    return self._tree.range_sum(begin + 1, end + 1)
