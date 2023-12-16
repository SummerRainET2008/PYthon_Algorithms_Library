# ListNode:

1. ___\_\_init\_\_(self, content)___
1. ___next(self)___-> ListNode
1. ___prev(self)___-> ListNode
1. ___get(self)___-> content
1. ___set(self, content)___

# LinkedList

1. ___\_\_init\_\_(self)___
1. ___to_list(self)___
   * Convert to a Python list.
1. ___size(self)___
   * You can also use pythonic function `len()`..
1. ___push_front(self, content)___
1. ___push_back(self, content)___
1. ___pop_front(self)___
1. ___pop_back(self)___
1. ___begin(self)___-> ListNode
1. ___end(self)___->ListNode
1. ___rbegin(self)___
   * This is the first position in a reversed List, just like C++ STL does.
1. ___rend(self)___
   * This is the dummy end node in a reversed List, just like C++ STL does.
1. ___insert_element(self, pos_node: ListNode, e)___
   * Insert a new node with value `e` before the `pos_node`.
1. ___insert(self, pos_node: ListNode, node: ListNode)___
   * Insert the node `node` before the `pos_node`.
1. ___remove(self, node: ListNode)___
2. ___index(self, content)___-> ListNode

