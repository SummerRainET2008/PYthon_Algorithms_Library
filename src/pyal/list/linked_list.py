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

  def get(self, index) -> ListNode:
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

  def clear(self):
    if self._num == 0:
      return

    self.get(0)._next = self.get(-1)._prev = None
    self._fake_head._next = self._fake_tail
    self._fake_tail._prev = self._fake_head
    self._num = 0

  def to_list(self):
    ans = []
    node = self.begin()
    while node is not self.end():
      ans.append(node.get())
      node = node.next()

    return ans

  def __len__(self):
    return self.size()

  def size(self):
    return self._num

  def push_front(self, content):
    self.insert(self.begin(), ListNode(content))

  def push_back(self, content):
    self.insert(self.end(), ListNode(content))

  def extend(self, second_list):
    '''
    :param second_list: can be a python list, or LinkedList
    :return:
    '''
    if isinstance(second_list, list):
      for d in second_list:
        self.push_back(d)
    elif isinstance(second_list, LinkedList):
      self.extend(second_list.to_list())
    else:
      assert False, "second_list must be [list, LinkedList]"

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

  def first_element(self):
    assert self._num > 0
    return self.begin().get()

  def last_element(self):
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

  def insert_element(self, pos_node: ListNode, e)-> ListNode:
    return self.insert(pos_node, ListNode(e))

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

    return node

  def remove(self, node: ListNode)-> ListNode:
    self._check_node_validity(node)

    nd1, nd2, nd3 = node._prev, node, node._next
    nd1._next = nd3
    nd3._prev = nd1
    nd2._prev = nd2._next = None
    self._num -= 1

    return nd3

  def index(self, content) -> ListNode:
    '''
    :param content:
    :return: node if it exists else None
    '''
    node = self.begin()
    while node is not self.end():
      if node.get() == content:
        return node
      node = node.next()

    return None

  def rindex(self, content)-> ListNode:
    node = self.rbegin()
    while node is not self.rend():
      if node.get() == content:
        return node
      node = node.prev()

    return None

  def clone(self):
    new_list = LinkedList()
    new_list.extend(self)
    return new_list

  def reversed(self):
    new_list = LinkedList()
    new_list.extend(list(reversed(self.to_list())))
    return new_list
