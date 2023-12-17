# Tree 

1. ___\_\_init____(self)
    > ```python
    > import pyal
    > tree = pyal.TreeMap()
    >```
1. ___\_\_setitem_____(self, key, value)
   > ```python
   > tree[0] = "Hello"
   > tree[1] = "World"
   > tree[2] = "This"
   > tree[3] = "is"
   > tree[4] = "from"
   > tree[5] = "pyal"
   > tree[6] = "library"
   > ```
1. ___\_\_getitem_____(self, key)-> value
   > ```python
   > print(tree[0]) # "Hello"
   > print(tree[1]) # "World"
   >  ```
1. ___size___(self)-> int
   > ```python
   > print(tree.size())   # 7 
   > print(len(tree))     # 7 
   >  ```

1. ___keys___(self)-> iter
   > ```python
   > #Example
   > keys = list(tree.keys())    # keys = [0, 1, 2, 3, 4, 5, 6]
   > ```

1. ___items___(self)-> iter
   > ```python
   > for key, value in tree.items():
   >    print(f"key={key}, value={value}")
   > ```
   > output
   > ```python
   > key=0, value=Hello
   > key=1, value=World
   > key=2, value=This
   > key=3, value=is
   > key=4, value=from
   > key=5, value=pyal
   > key=6, value=library
   > ```
1. ___key_list_begin___(self)

   > All keys are organized in an sorted order stored in a [LinkedList](example_LinkedList.md). To get the value stored
   in some node, we can use `ListNode.get()` operation. 
   >   
   > With this function, you can operate keys more flexibly. 
   > ```python
   > key_list_node = tree.key_list_begin()
   > while key_list_node is not tree.key_list_end():
   >    print(f"key={key_list_node.get()}")
   >    key_list_node = key_list_node.next()
   > ```
   > output
   > ```python
   > key=0
   > key=1
   > key=2
   > key=3
   > key=4
   > key=5
   > key=6
   > ```

1. ___key_list_end___(self)
                  
   > It is a dummy node that just denotes the end of a list. 
   > Usually you use `node is not tree.key_list_end()` to know whether it reaches the end. 
   > This aligns with C++ STL style.
      
1. ___lower_bound___(self, key)
                  
   > It returns the first ListNode whose key is not smaller than the input key. 
   > You can use `ListNode.prev()` or `ListNode.next()` to traverse the remaining tree.
   >    
   > ```python
   > lower_bound_node = tree.lower_bound(4.5)
   > lower_bound_key = lower_bound_node.get()        # 5
   > lower_bound_value = tree[lower_bound_key]   # pyal
   > next_node = lower_bound_node.next()         # pointing to <6, library>
   > print(next_node.get())
   > ```
1. ___upper_bound___(self, key)
                  
   > It returns the first ListNode whose key is greater than the input key.
   > ```python
   > upper_bound_node = tree.upper_bound(5)
   > upper_bound_key = upper_bound_node.get()        # 6
   > print(upper_bound_key)
   > ```
1. ___get___(self, key, default_value=None)
                  
   > If you know the element exists in the map, you can just use `TreeMap[key]`, or
   > use this function with a default value when absent.
   
1. ___remove___(self, key)
             
   > This function would not throw an exception whether the key exists or not.
       

