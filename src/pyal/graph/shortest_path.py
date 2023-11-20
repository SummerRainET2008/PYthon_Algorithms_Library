from pyal.graph.graph import Graph
from pyal.tree.dynamic_heap import DynamicHeap
from pyal.common.algorithm import INF


class Dijkstra:
  def __init__(self, graph: Graph, source_vertex: int):
    assert source_vertex in graph.vertexes()

    self._source = source_vertex
    heap = DynamicHeap()
    self._opt_dist = {source_vertex: 0}
    self._opt_in_edge = {}

    for v in graph.vertexes():
      if v not in self._opt_dist:
        dist = graph.get_weight(source_vertex, v)
        dist = INF if dist is None else dist
        heap.push(v, dist)
        self._opt_in_edge[v] = source_vertex

    while heap.size() > 0:
      top = heap.pop()
      v, dist = top.id, top.value
      self._opt_dist[v] = dist

      for edge in graph.get_out_edges(v):
        if edge.v2 in self._opt_dist:
          continue

        old_value = heap.get(edge.v2)
        new_value = dist + edge.weight
        if new_value < old_value:
          heap.update(edge.v2, new_value)
          self._opt_in_edge[edge.v2] = edge.v1

  def get_min_distance(self, target_vertex: int):
    return self._opt_dist.get(target_vertex, None)

  def get_optimal_paths(self, target_vertex: int):
    paths = []
    while target_vertex != self._source:
      paths.append(target_vertex)
      target_vertex = self._opt_in_edge[target_vertex]
    paths.append(self._source)
    paths = paths[::-1]

    return paths
