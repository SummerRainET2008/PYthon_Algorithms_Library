from pyal.graph.graph import Graph
from pyal.graph.shortest_path import Dijkstra


def test_dijkstra():
  graph = Graph()
  graph.set_edge(1, 2, 7, directed_edge=False)
  graph.set_edge(1, 3, 9, directed_edge=False)
  graph.set_edge(1, 6, 14, directed_edge=False)
  graph.set_edge(2, 3, 10, directed_edge=False)
  graph.set_edge(2, 4, 15, directed_edge=False)
  graph.set_edge(3, 4, 11, directed_edge=False)
  graph.set_edge(3, 6, 2, directed_edge=False)
  graph.set_edge(4, 5, 6, directed_edge=False)
  graph.set_edge(5, 6, 9, directed_edge=False)

  source = 1
  dij = Dijkstra(graph, source)
  for v in [1, 2, 3, 4, 5, 6]:
    print(f"source: {source}, target: {v}, "
          f"min_distance={dij.get_min_distance(v)}, "
          f"optimal paths={dij.get_optimal_paths(v)}")
