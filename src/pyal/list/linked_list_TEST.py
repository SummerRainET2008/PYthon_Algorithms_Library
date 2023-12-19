from pyal.list.linked_list import LinkedList, ListNode


def test_list():
  list = LinkedList()
  list.push_front(1)
  assert list.begin().get() == 1

  list.push_back(2)
  assert list.rbegin().get() == 2

  assert list.size() == 2
  assert list.to_list() == [1, 2]

  list.push_back(3)
  print("list:", list.to_list())
  assert list.get_element(-1) == 3
  assert list.get(1).get() == 2

  list.clear()
  assert list.to_list() == []

  assert list.index(3) is None

  list.push_back(1)
  list.push_back(3)
  list.push_back(5)
  assert list.index(4) is None
  assert list.index(5).prev().prev().get() == 1
  assert list.rindex(5).prev().prev().get() == 1

  clone_list = list.clone()
  clone_list.extend([2, 4, 6])
  assert clone_list.to_list() == [1, 3, 5, 2, 4, 6]

  second_list = LinkedList()
  second_list.extend([2, 4, 6])
  clone_list = list.clone()
  clone_list.extend(second_list)
  assert clone_list.to_list() == [1, 3, 5, 2, 4, 6]
  assert clone_list.reversed().to_list() == [6, 4, 2, 5, 3, 1]

def test_insertion():
  list = LinkedList()
  list.push_back(1)
  list.push_back(2)
  list.push_back(3)
  list.push_back(4)
  node = list.insert_element(list.begin(), 0)
  assert node.get() == 0
  list.insert(list.rbegin(), ListNode(100))
  assert list.to_list() == [0, 1, 2, 3, 100, 4]

  iter = list.begin()
  iter = iter.next()
  next_node = list.remove(iter)
  assert next_node.get() == 2

  data = []
  iter = list.begin()
  while iter is not list.end():
    data.append(iter.get())
    iter = iter.next()

  assert data == [0, 2, 3, 100, 4]

  list.get(3).set(3.5)
  assert list.get(3).get() == 3.5

  data = []
  iter = list.rbegin()
  while iter is not list.rend():
    data.append(iter.get())
    iter = iter.prev()

  assert data == [0, 2, 3, 3.5, 4][::-1]
