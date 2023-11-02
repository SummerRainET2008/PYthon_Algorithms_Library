from pyal.graph.graph import Graph
from pyal.graph.shortest_path import dijkstra

def test_dijkstra():
  graph = Graph()
  graph.set_edge(1, 2,  7, directed_edge=False)
  graph.set_edge(1, 3,  9, directed_edge=False)
  graph.set_edge(1, 6, 14, directed_edge=False)
  graph.set_edge(2, 3, 10, directed_edge=False)
  graph.set_edge(2, 4, 15, directed_edge=False)
  graph.set_edge(3, 4, 11, directed_edge=False)
  graph.set_edge(3, 6,  2, directed_edge=False)
  graph.set_edge(4, 5,  6, directed_edge=False)
  graph.set_edge(5, 6,  9, directed_edge=False)

  dist = dijkstra(graph, 1)
  print(dist)
  assert dist[5] == 20
  assert dist[4] == 20

if __name__ == "__main__":
  test_dijkstra()
