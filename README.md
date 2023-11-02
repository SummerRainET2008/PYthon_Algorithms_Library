# PYthon Algorithms Library

Python does not have some useful or important data structures, like linked list, tree map, just like STL in C++. 
This library, PYthon Algorithm Library (pyal), aims to provide a python version substitue of STL in C++.

# 1. Examples

Balanced search tree based map, ```TreeMap```

```python
import pyal

tree_map = pyal.TreeMap()
data = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e"), (5, "f")]
for key, value in data:
    tree_map.set(key, value)

key = 0
print(f"{key=}, value={tree_map.get(key)=}")

key = 1
node = tree_map.lower_bound(key)
print(f"lower_bound({key=}): {node()=}")

node = tree_map.upper_bound(key)
print(f"upper_bound({key=}): {node()=}")

print(f"min key: {tree_map.key_list_begin()()}")
print(f"max key: {tree_map.key_list_end().prev()()}")

```

Output
```
key=0, value=tree_map.get(key)='a'
lower_bound(key=1): node()=1
upper_bound(key=1): node()=2
min key: 0
max key: 5
```


# 2. Popular data structures and algorithms.
  * Tree
    >* TreeMap [example](src/doc/example_TreeMap.md)
    >   * balanced AVL tree, `insert` & `delete`: O(log N), `get`: O(1)
    >* DaynamicHeap [example](src/doc/example_DynamicHeap.md)
    >   * `update`, `deletion`: O(log N)
    >* MinHeap [example](src/doc/example_MinHeap.md)
    >* DisjointSet [example](src/doc/example_DisjointSet.md)
  * list
    > * LinkedList [example](src/doc/example_DisjointSet.md)
    > * Queue [example](src/doc/example_DisjointSet.md)
    > * Dequeue [example](src/doc/example_DisjointSet.md)
    > * Stack [example](src/doc/example_DisjointSet.md)
    > * LRUCache [example](src/doc/example_DisjointSet.md)
    >   * `get` & `set`: O(1)
    > * LFUCache [example](src/doc/example_DisjointSet.md)
    >   * `get` & `set`: O(1) 
  * String
  * Graph
  * Common useful functions. 
