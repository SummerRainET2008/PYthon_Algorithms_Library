from pyal.graph.graph import Graph
from pyal.graph.topological_traversal import topological_traversal


def test_topological_traversal():
  graph = Graph()
  graph.set_edge(1, 2, 1.0)
  graph.set_edge(2, 3, 1.0)
  graph.set_edge(3, 4, 1.0)
  graph.set_edge(1, 2, 1.0)

  vertexes = list(topological_traversal(graph))
  assert vertexes[0] == [4]
  assert vertexes[1] == [3]
  assert vertexes[2] == [2]
