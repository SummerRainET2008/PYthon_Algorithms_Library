# ListNode:

1. def __init__(self, content):

1. def next(self):

1. def prev(self):

# LinkedList

1. `__init__(self)`
1. `to_list(self)`
                   
   Convert to a Python list.
       
1. `size(self)`
1. `push_front(self, content)`
1. `push_back(self, content)`
1. `pop_front(self)`
1. `pop_back(self)`
1. `begin(self)`
1. `end(self)`
1. `rbegin(self)`
                 
   This is the first position in a reversed List, just like C++ STL does.
       
1. `rend(self)`
                  
   This is the dummy end node in a reversed List, just like C++ STL does.
       
1. `insert_element(self, pos_node: ListNode, e)`
                  
   Insert a new node with value `e` before the `pos_node`.
       
1. `insert(self, pos_node: ListNode, node: ListNode)`
                  
   Insert the node `node` before the `pos_node`.
       
1. `remove(self, node: ListNode)`