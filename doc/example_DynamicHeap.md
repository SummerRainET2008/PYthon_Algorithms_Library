# DynamicHeap

In some search senarios, we need to update or delete some value stored in a heap. 
Such as `Dijkstra algorithm`, nodes are stored in a heap by their current
shortest distance values from the source vertex. These values are updated by the selected optimal vertex in each iteration. The algorithm example from a textbook often uses a `for[example_DynamicHeap.md](example_DynamicHeap.md)-loop` to select the optimal vertex to demonstrate the core idea. 

We can instead use DynamicHeap to speed up this part. Then the `id` is the vertex index, which can be `int` or `string`; `value` is its correspondong shortest distance. 
You can update or delete some vertex without reconstructing a heap or a `for-loop`.

If your application does not have such requiremnts, and permits duplicate values stored
in the heap, you should use `pyal.Heap`, which is a simple OOD encapsulation of Python 
heap related functions.

1. `__init__(self)`
1. `size(self)`
1. `top(self)`
   
   Return the smallest value without removing it.   
1. `push(self, id, value)`
1. `pop(self)`
                   
   Return the smallest value and remove it.
    
1. `get(self, id)`
1. `remove(self, id)`
1. `update(self, id, value)`
