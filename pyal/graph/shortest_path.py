from .graph import Graph
from ..tree.dynamic_heap import DynamicHeap
from ..common.algorithm import INF

def dijkstra(graph: Graph, source: int):
  heap = DynamicHeap()
  opt_dist = {source: 0}
  for v in graph.vertexes():
    if v not in opt_dist:
      dist = graph.get_weight(source, v)
      dist = INF if dist is None else dist
      heap.push(v, dist)

  while heap.size() > 0:
    top = heap.pop()
    v, dist = top.id, top.value
    opt_dist[v] = dist

    for edge in graph.get_out_edges(v):
      if edge.v2 in opt_dist:
        continue

      old_value = heap.get(edge.v2).value
      new_value = dist + edge.weight
      if new_value < old_value:
        heap.update(edge.v2, new_value)

  return opt_dist

