import collections


class Graph:
  Edge = collections.namedtuple("Edge", ["v1", "v2", "weight"])

  def __init__(self):
    self._out_edges = {}
    self._in_edges = {}
    self._vertexes = set()

  def clone(self):
    import copy
    return copy.deepcopy(self)

  def get_out_edges_size(self, vertex):
    return len(self._out_edges.get(vertex, {}))

  def get_in_edges_size(self, vertex):
    return len(self._in_edges.get(vertex, {}))

  def get_out_edges(self, vertex):
    for v2, w in self._out_edges.get(vertex, {}).items():
      yield Graph.Edge(v1=vertex, v2=v2, weight=w)

  def get_in_edges(self, vertex):
    for v1, w in self._in_edges.get(vertex, {}).items():
      yield Graph.Edge(v1=v1, v2=vertex, weight=w)

  def print(self):
    print("Graph:")
    for edge in self.edges():
      print(edge)
    print()

  def vertexes(self) -> set:
    return set(self._vertexes)

  def get_weight(self, vertex1: int, vertex2: int):
    if vertex1 not in self._out_edges:
      return None
    return self._out_edges[vertex1].get(vertex2, None)

  def edges(self):
    for v1 in self._out_edges:
      for v2, w in self._out_edges[v1].items():
        yield Graph.Edge(v1=v1, v2=v2, weight=w)

  def remove_edge(self, vertex1: int, vertex2: int):
    try:
      del self._out_edges[vertex1][vertex2]
    except:
      pass

    try:
      del self._in_edges[vertex2][vertex1]
    except:
      pass

  def set_edge(self,
               vertex1: int,
               vertex2: int,
               weight: float,
               directed_edge: bool = True):
    self._vertexes.add(vertex1)
    self._vertexes.add(vertex2)
    self._out_edges.setdefault(vertex1, {})[vertex2] = weight
    self._in_edges.setdefault(vertex2, {})[vertex1] = weight

    if not directed_edge:
      self.set_edge(vertex2, vertex1, weight, directed_edge=True)
