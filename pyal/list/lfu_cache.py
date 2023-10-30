from .linked_list import ListNode, LinkedList

debug = False
# debug = True

class MainValue:
  def __init__(self, freq):
    self.list = LinkedList()
    self.freq = freq

class AuxValue:
  def __init__(self, key, value, freq, main_node):
    self.key = key
    self.value = value
    self.freq = freq
    self.main_node = main_node

class LFUCache:
  def __init__(self, capacity: int):
    self._list = LinkedList()
    self._key2aux_node = {}
    self._capacity = capacity

  def _get_size(self):
    return len(self._key2aux_node)

  def get(self, key: int) -> int:
    if debug:
      print(f"get({key})")
    auxnode = self._key2aux_node.get(key, None)
    if auxnode is None:
      return -1

    auxnode().freq += 1
    self._update_position(auxnode)
    return auxnode().value

  def _update_position(self, auxnode):
    main_node = auxnode().main_node
    main_node().list.remove(auxnode)

    if main_node is self._list.begin() or \
      main_node.prev()().freq != auxnode().freq:
      self._list.insert(main_node, ListNode(MainValue(auxnode().freq)))

    main_node = main_node.prev()
    auxnode().main_node = main_node
    main_node().list.insert(main_node().list.begin(), auxnode)

    if main_node.next()().list.size() == 0:
      self._list.remove(main_node.next())

  def put(self, key: int, value: int) -> None:
    if debug:
      print(f"put({key}, {value})")

    auxnode = self._key2aux_node.get(key, None)
    if auxnode is not None:
      auxnode().value = value
      auxnode().freq += 1
      self._update_position(auxnode)

    else:
      if self._get_size() == self._capacity:
        last_mainvalue = self._list.rbegin()()
        last_key = last_mainvalue.list.pop_back().key
        del self._key2aux_node[last_key]
        if debug:
          print(f"removing {last_key}")

        if last_mainvalue.list.size() == 0:
          self._list.pop_back()

      if not (self._list.size() > 0 and self._list.rbegin()().freq == 1):
        self._list.push_back(MainValue(1))

      last_mainnode = self._list.rbegin()
      auxnode_value = AuxValue(key, value, 1, last_mainnode)
      last_mainnode().list.push_front(auxnode_value)
      self._key2aux_node[key] = last_mainnode().list.begin()

def main():
  # solu = LFUCache(2)
  # solu.put(1, 1)
  # solu.put(2, 2)
  # print(solu.get(1))
  # solu.put(3, 3)
  # print(solu.get(2))
  # print(solu.get(3))
  # print(solu.put(4, 4))
  # print(solu.get(1))
  # print(solu.get(3))
  # print(solu.get(4))

  solu = None
  # user_input = [[3],[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[2],[3],[4],[5]]
  user_input1 = ["LFUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
  user_input2 = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
  for opeator, item in zip(user_input1, user_input2):
    if opeator == "LFUCache":
      solu = LFUCache(item[0])
    elif len(item) == 1:
      print(solu.get(item[0]))
    else:
      solu.put(item[0], item[1])

if __name__ == "__main__":
  main()

