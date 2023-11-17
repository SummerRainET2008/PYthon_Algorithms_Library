'''
Author: Tian Xia (TianXia0209@gmail.com)
'''

from pyal.list.linked_list import LinkedList

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
      self._list.insert_element(main_node, MainValue(auxnode().freq))

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
