from pyal.graph.graph import Graph


def topological_traversal(graph: Graph) -> iter:
  '''
  :return: an iterator of vertex list each time.
  '''
  graph = graph.clone()
  empty_set = [v for v in graph.vertexes() if graph.get_out_edges_size(v) == 0]

  while len(empty_set) > 0:
    yield list(empty_set)

    new_empty_set = set()
    for v2 in empty_set:
      in_edges = list(graph.get_in_edges(v2))
      for edge in in_edges:
        graph.remove_edge(edge.v1, edge.v2)
        if graph.get_out_edges_size(edge.v1) == 0:
          new_empty_set.add(edge.v1)

    empty_set = new_empty_set
