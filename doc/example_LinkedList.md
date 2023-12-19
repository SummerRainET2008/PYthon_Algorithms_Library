# ListNode:

1. ___\_\_init_____(self, content)
1. ___next___(self)-> ListNode
1. ___prev___(self)-> ListNode
1. ___get___(self)-> content
1. ___set___(self, content)

# LinkedList

1. ___\_\_init_____(self)
1. ___to_list___(self)-> list
   * Convert to a Python list.
1. ___size___(self)-> int
   * You can also use pythonic function `len()`..
1. ___push_front___(self, content)
1. ___push_back___(self, content)
1. ___pop_front___(self)-> content
1. ___pop_back___(self)-> content
1. ___begin(self)___-> ListNode
1. ___end(self)___->ListNode
1. ___rbegin(self)___-> ListNode
   * This is the first position in a reversed List, just like C++ STL does.
1. ___rend(self)___-> ListNode
   * This is the dummy end node in a reversed List, just like C++ STL does.
1. ___insert_element___(self, pos_node: ListNode, e)-> ListNode
   * Insert a new node with value `e` before the `pos_node`.
1. ___insert___(self, pos_node: ListNode, node: ListNode)-> ListNode
   * Insert the node `node` before the `pos_node`.
1. ___remove___(self, node: ListNode)-> ListNode
1. ___index___(self, content)-> ListNode or None
1. ___rindex___(self, content)-> ListNode or None
1. ___extend___(self, second_list: typing.Union[list, LinkedList])
1. ___clone___(self)-> ListList
1. ___reversed___(self)-> ListList

