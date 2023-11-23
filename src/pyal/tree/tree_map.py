'''
Author: Tian Xia (TianXia0209@gmail.com)
'''

from pyal.list.linked_list import LinkedList


class _AVLTreeNode:
  def __init__(self, key: int):
    self._key = key
    self._left = None
    self._right = None
    self._depth = 1
    self._next_value = None

  def _print_tree(self):
    import nltk
    tree_expr = str(self)
    tree = nltk.Tree.fromstring(tree_expr)
    tree.pretty_print()
    print()

  def __str__(self):
    if self._left is not None:
      left = str(self._left)
    else:
      left = "(null)"
    if self._right is not None:
      right = str(self._right)
    else:
      right = "(null)"

    return f"({self._key} {left} {right})"

  def _debug_checked_depth(self):
    if self._left is None and self._right is None:
      return 1
    elif self._left is None:
      rd = self._right._debug_checked_depth()
      assert rd < 2
      return rd + 1
    elif self._right is None:
      ld = self._left._debug_checked_depth()
      assert ld < 2
      return ld + 1
    else:
      ld = self._left._debug_checked_depth()
      rd = self._right._debug_checked_depth()
      assert abs(ld - rd) < 2
      return max(ld, rd) + 1

  def _find_lower_bound(self, key):
    if key == self._key:
      return self
    elif key < self._key:
      if self._left is not None:
        node = self._left._find_lower_bound(key)
        return self if node is None else node
      return self
    else:
      if self._right is not None:
        return self._right._find_lower_bound(key)
      return None

  def _insert(self, key, next_key: list, from_left: bool):
    assert key != self._key

    if key < self._key:
      next_key[0] = self._key
      if self._left is None:
        self._left = _AVLTreeNode(key)
      else:
        self._left = self._left._insert(key, next_key, True)

    else:
      if self._right is None:
        self._right = _AVLTreeNode(key)
      else:
        self._right = self._right._insert(key, next_key, False)

    return _AVLTreeNode._reset_balance(self, from_left)

  def _is_balanced(self, from_left: bool):
    bf = self._get_balance_factor()
    return bf == 0 or (from_left and bf == 1) or (not from_left and bf == -1)

  def _get_balance_factor(self):
    return self._get_depth(self._left) - self._get_depth(self._right)

  @staticmethod
  def _reset_node(node, from_left: bool):
    node._reset_depth()
    bf = node._get_balance_factor()

    if bf == -2:
      return node._left_rotate()

    elif bf == -1:
      return node if not from_left else node._left_rotate()

    elif bf == 0:
      return node

    elif bf == 1:
      return node if from_left else node._right_rotate()

    elif bf == 2:
      return node._right_rotate()

    else:
      assert False

  @staticmethod
  def _reset_balance(node, from_left: bool):
    if node is None:
      return node

    new_root = node
    while True:
      new_root = _AVLTreeNode._reset_node(new_root, from_left)
      if new_root._is_balanced(from_left):
        return new_root

  def _right_rotate(self):
    bf = self._get_balance_factor()
    # assert bf >= 2

    left = self._left
    self._left = _AVLTreeNode._reset_balance(left._right, True)
    self._reset_depth()

    left._right = _AVLTreeNode._reset_balance(self, False)
    left._reset_depth()

    return left

  def _get_depth(self, node):
    return 0 if node is None else node._depth

  def _reset_depth(self):
    self._depth = max(self._get_depth(self._left), self._get_depth(
        self._right)) + 1

  def _left_rotate(self):
    bf = self._get_balance_factor()
    # assert bf <= -2

    right = self._right
    self._right = _AVLTreeNode._reset_balance(right._left, False)
    self._reset_depth()

    right._left = _AVLTreeNode._reset_balance(self, True)
    right._reset_depth()

    return right

  def _remove(self, key, from_left: bool):
    # Key must be existent
    if key < self._key:
      self._left = self._left._remove(key, True)
      return self
    elif key > self._key:
      self._right = self._right._remove(key, False)
      return self

    else:
      if self._right is None:
        return _AVLTreeNode._reset_balance(self._left, from_left)
      elif self._left is None:
        return _AVLTreeNode._reset_balance(self._right, from_left)
      else:
        left_right_list = []
        node = self._left
        while node is not None:
          left_right_list.append(node)
          node = node._right

        left_right_list[-1]._right = self._right._left
        while left_right_list != []:
          left_right_list[-1]._right = _AVLTreeNode._reset_balance(
              left_right_list[-1]._right, False)
          left_right_list.pop()

        self._right._left = self._left
        return _AVLTreeNode._reset_balance(self._right, from_left)


class TreeMap:
  def __init__(self):
    from collections import namedtuple

    self._root = None
    self._key_list = LinkedList()

    self._KeyInfo = namedtuple("KeyInfo", ["value", "key_list_node"])
    self._key2info = {}  # {"key": KeyInfo}

  def size(self):
    return self._key_list.size()

  def _print_tree(self):
    if self._root is None:
      print("null-tree")
    else:
      self._root._print_tree()

  def keys(self) -> iter:
    node = self._key_list.begin()
    while node is not self._key_list.end():
      yield node.get()
      node = node.next()

  def items(self) -> iter:
    for key in self.keys():
      yield key, self.get(key)

  def key_list_begin(self):
    return self._key_list.begin()

  def key_list_end(self):
    return self._key_list.end()

  def lower_bound(self, key):  # return key_list node
    if self._root is None:
      return self.key_list_end()

    node = self._root._find_lower_bound(key)
    if node is None:
      return self._key_list.end()

    return self._key2info[node._key].key_list_node

  def upper_bound(self, key):
    node = self.lower_bound(key)
    if node is self.key_list_end() or key < node.get():
      return node

    return node.next()

  def get(self, key, default_value=None):
    info = self._key2info.get(key, None)
    return default_value if info is None else info.value

  def remove(self, key):
    info = self._key2info.get(key, None)
    if info is None:
      return

    self._key_list.remove(info.key_list_node)
    del self._key2info[key]
    self._root = self._root._remove(key, True)

  def __getitem__(self, key):
    return self._key2info[key].value

  def __setitem__(self, key, value):
    rd = self._key2info.get(key, None)
    if rd is not None:
      self._key2info[key] = rd._replace(value=value)
      return

    if self._root is None:
      self._root = _AVLTreeNode(key)
      self._key_list.push_back(key)
      self._key2info[key] = self._KeyInfo(
          value=value, key_list_node=self._key_list.rbegin())

    else:
      next_key = [None]
      self._root = self._root._insert(key, next_key, True)

      if next_key[0] is None:
        next_node = self._key_list.end()
      else:
        next_node = self._key2info[next_key[0]].key_list_node
      self._key_list.insert_element(next_node, key)

      self._key2info[key] = self._KeyInfo(value=value,
                                          key_list_node=next_node.prev())
