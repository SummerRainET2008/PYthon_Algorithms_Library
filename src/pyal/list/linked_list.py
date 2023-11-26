'''
Author: Tian Xia (TianXia0209@gmail.com)
'''


class ListNode:
  def __init__(self, content):
    self._prev = None
    self._next = None
    self._content = content

  def next(self):
    return self._next

  def prev(self):
    return self._prev

  def set(self, content):
    self._content = content

  def get(self):
    return self._content


class LinkedList:
  def __init__(self):
    self._fake_head = ListNode(None)
    self._fake_tail = ListNode(None)
    self._fake_head._next = self._fake_tail
    self._fake_tail._prev = self._fake_head
    self._num = 0

  def get(self, index)-> ListNode:
    if index < 0:
      assert 1 <= -index <= self.size()
      index += self.size()
    assert 0 <= index < self.size()

    if index == 0:
      return self.begin()
    elif index == self.size() - 1:
      return self.rbegin()
    else:
      node = self.begin()
      for _ in range(index):
        node = node.next()
      return node

  def get_element(self, index):
    return self.get(index).get()


  def to_list(self):
    ans = []
    node = self.begin()
    while node is not self.end():
      ans.append(node.get())
      node = node.next()

    return ans

  def size(self):
    return self._num

  def push_front(self, content):
    self.insert(self.begin(), ListNode(content))

  def push_back(self, content):
    self.insert(self.end(), ListNode(content))

  def pop_front(self):
    assert self._num > 0
    value = self.begin().get()
    self.remove(self.begin())
    return value

  def pop_back(self):
    assert self._num > 0
    value = self.rbegin().get()
    self.remove(self.rbegin())
    return value

  def front(self):
    assert self._num > 0
    return self.begin().get()

  def back(self):
    assert self._num > 0
    return self.rbegin().get()

  def begin(self):
    return self._fake_head._next

  def end(self):
    return self._fake_tail

  def rbegin(self):
    return self._fake_tail._prev

  def rend(self):
    return self._fake_head

  def insert_element(self, pos_node: ListNode, e):
    self.insert(pos_node, ListNode(e))

  def _check_node_validity(self, node):
    assert node is not None
    assert node not in [self._fake_head, self._fake_tail]

  def insert(self, pos_node: ListNode, node: ListNode):
    self._check_node_validity(node)

    nd1, nd2, nd3 = pos_node._prev, node, pos_node
    nd1._next = nd2
    nd2._prev = nd1
    nd2._next = nd3
    nd3._prev = nd2
    self._num += 1

  def remove(self, node: ListNode):
    self._check_node_validity(node)

    nd1, nd2, nd3 = node._prev, node, node._next
    nd1._next = nd3
    nd3._prev = nd1
    nd2._prev = nd2._next = None
    self._num -= 1
