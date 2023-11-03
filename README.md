# PYthon Algorithms Library

Python does not have some useful or important data structures, like linked list, tree map, just like STL in C++. 
This library, PYthon Algorithm Library (pyal), aims to provide a python version substitue of STL in C++.

# 1. Install [github](https://github.com/SummerRainET2008/PYthon_Algorithms_Library)
 ```bash
 python3 -m pip install Python-Algorithm-pyal
 ```

# 2. Examples

Balanced search tree based map, ```TreeMap```

```python
import pyal

def main():
  tree_map = pyal.TreeMap()
  data = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e"), (5, "f")]
  for key, value in data:
    tree_map[key] = value

  key = -1
  value = tree_map.get(key)
  if value is None:
    print(f"key={key} does not exist")

  key = 0
  print(f"key={key}, value={tree_map[key]}")

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
key=-1 does not exist
key=0, value=a
lower_bound(key=1): node()=1
upper_bound(key=1): node()=2
min key: 0
max key: 5
```


# 3. Popular data structures and algorithms.
  Please check [github](https://github.com/SummerRainET2008/PYthon_Algorithms_Library) for all examples.
  * Tree
    >* TreeMap [example](doc/example_TreeMap.md)
    >   * balanced AVL tree, `insert` & `delete`: O(log N), `get`: O(1)
    >* DaynamicHeap [example](doc/example_DynamicHeap.md)
    >   * `update`, `deletion`: O(log N)
    >* MinHeap [example](doc/example_MinHeap.md)
    >* DisjointSet [example](doc/example_DisjointSet.md)
  * list
    > * LinkedList [example](doc/example_DisjointSet.md)
    > * Queue [example](doc/example_DisjointSet.md)
    > * Dequeue [example](doc/example_DisjointSet.md)
    > * Stack [example](doc/example_DisjointSet.md)
    > * LRUCache [example](doc/example_DisjointSet.md)
    >   * `get` & `set`: O(1)
    > * LFUCache [example](doc/example_DisjointSet.md)
    >   * `get` & `set`: O(1) 
  * String
  * Graph
  * Common useful functions. 
