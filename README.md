# PYthon Algorithms Library (pyal)

Python does not have some useful or important data structures, like `linked list`, `tree map`, just like STL in C++. 
This library aims to provide a python counterpart of C++ STL.

# 1. Install 
 ```bash
 python3 -m pip install Python-Algorithm-pyal
 ```

# 2. Examples [github](https://github.com/SummerRainET2008/PYthon_Algorithms_Library)

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
  print(f"lower_bound({key=}): {node.get()=}")

  node = tree_map.upper_bound(key)
  print(f"upper_bound({key=}): {node.get()=}")

  print(f"min key: {tree_map.key_list_begin().get()}")
  print(f"max key: {tree_map.key_list_end().prev().get()}")
```

Output
```
key=-1 does not exist
key=0, value=a
lower_bound(key=1): node.get()=1
upper_bound(key=1): node.get()=2
min key: 0
max key: 5
```


# 3. Popular data structures and algorithms.
  Please check [github](https://github.com/SummerRainET2008/PYthon_Algorithms_Library) for all examples.
  * ### Tree
    >* TreeMap [example](doc/example_TreeMap.md)
    >   * ___Balanced___ binary search tree.
    >   * ___insert___ & ___delete___: O(log N)
    >   * ___get___:  O(1)
    >* DynamicHeap [example](doc/example_DynamicHeap.md)
    >   * ___update___ & ___deletion___: O(log N)
    >* MinHeap, MaxHeap [example](doc/example_MinHeap.md)
    >* DisjointSet [example](doc/example_DisjointSet.md)
  * ### List
    > * LinkedList [example](doc/example_LinkedList.md)
    > * Queue [example](doc/example_Queue.md)
    > * Dequeue [example](doc/example_Deque.md)
    > * Stack [example](doc/example_Stack.md)
    > * LRUCache [example](doc/example_LRUCache.md)
    >   * ___get___ & ___set___: O(1)
    > * LFUCache [example](doc/example_LFUCache.md)
    >   * `get` & `set`: O(1) 
  * ### String
    >* search_KMP
    >* search_multipatterns
    >  * todo
  * ### Graph
    > * Graph
    > * Dijkstra
    > * topological_traversal
  * ### Common useful functions
    > * `is_none_or_empty`
    > * `histogram_ascii`
    > * `is_sorted` 
    > * `unique` 
    > * `cmp`
    > * `split_data_by_func` 
    > * `eq`
    > * `discrete_sample` 
    > * `group_by_key_fun` 
    > * `top_n`
    > * `clamp`
    > * `argmax`
    > * `argmin`
    > * `make_list`
    > * `swap`
    > * `rotate`
    > * `copy_to`
    > * `kth_smallest_element`
    > * `lower_bound`
    > * `upper_bound`
    > * `reverse_in_place`
    > * `sort_in_place`
    > * `find_first_if`
    > * `find_last_if`
    > * `next_permutation`
    > * `prev_permutation`
    > * `factorial`
    > * `combinatorial_number`
    > * `permutation_number`
    > * `combinations_with_duplicate`
    > * `longest_common_substr`
    > * `top_k_similar`
