from pyal.list.linked_list import LinkedList, ListNode


def test_list():
  list = LinkedList()
  list.push_front(1)
  assert list.begin().get() == 1

  list.push_back(2)
  assert list.rbegin().get() == 2

  assert list.size() == 2
  assert list.to_list() == [1, 2]


def test_insertion():
  list = LinkedList()
  list.push_back(1)
  list.push_back(2)
  list.push_back(3)
  list.push_back(4)
  list.insert_element(list.begin(), 0)
  list.insert(list.rbegin(), ListNode(100))

  iter = list.begin()
  iter = iter.next()
  list.remove(iter)

  data = []
  iter = list.begin()
  while iter is not list.end():
    data.append(iter.get())
    iter = iter.next()

  assert data == [0, 2, 3, 100, 4]

  data = []
  iter = list.rbegin()
  while iter is not list.rend():
    data.append(iter.get())
    iter = iter.prev()

  assert data == [0, 2, 3, 100, 4][::-1]
