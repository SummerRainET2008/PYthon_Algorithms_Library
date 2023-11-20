from pyal.graph.graph import Graph


def test_directional_graph():
  graph = Graph()
  graph.set_edge(1, 2, 1.0)
  graph.set_edge(2, 3, 1.0)
  graph.set_edge(3, 4, 1.0)
  graph.set_edge(1, 2, 1.0)

  graph.print()

  assert len(list(graph.get_in_edges(2))) == 1
  assert len(list(graph.get_out_edges(1))) == 1


def test_unidirectional_graph():
  graph = Graph()
  graph.set_edge(1, 2, 1.0, directed_edge=False)
  graph.set_edge(2, 3, 1.0, directed_edge=False)
  graph.set_edge(3, 4, 1.0, directed_edge=False)
  graph.set_edge(1, 2, 1.0, directed_edge=False)

  graph.print()
