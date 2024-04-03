'''
>> nosetests -v --nocapture test/tree_map_TEST.py
'''

from pyal.tree.tree_map import TreeMap
import random


def test_tree_construction():
  tree = TreeMap()
  random.seed(0)
  for _ in range(10):
    data = list(range(50))
    random.shuffle(data)
    print(f"test_tree_connstruction: {data=}")
    for d in data:
      tree[d] = d

    assert tree.size() == 50
    assert len(tree) == 50

    tree[0] = 100
    assert tree[0] == 100


def test_extreme_construction():
  tree = TreeMap()
  max_size = 10_000
  for d in range(max_size):
    tree[d] = d
  # tree._print_tree()
  assert tree.size() == max_size
  assert len(tree) == max_size


def test_lower_bound():
  tree = TreeMap()
  data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  test_data = data[::]
  random.shuffle(test_data)
  for d in test_data:
    tree[d] = d

  for p in range(len(data)):
    lower_node = tree.lower_bound(data[p] + 0.1)
    if p == len(data) - 1:
      assert lower_node is tree.key_list_end()
    else:
      assert lower_node.get() == data[p + 1]

    lower_node = tree.lower_bound(data[p] - 0.1)
    assert lower_node.get() == data[p]

  keys = list(tree.keys())
  assert keys == data


def test_one_remove():
  tree = TreeMap()
  data = [5, 4, 6, 3, 7, 2, 8, 1, 9, 0, 10]
  for d in data:
    tree[d] = d
  tree._print_tree()

  assert tree.first_key() == min(data)
  assert tree.last_key() == max(data)

  tree.remove(5)
  print(f"Removed 5")
  tree._print_tree()
  node = tree.lower_bound(5)
  assert node.get() == 6

  tree.remove(1)
  print(f"Removed 1")
  tree._print_tree()
  node = tree.lower_bound(0.1)
  assert node.get() == 2

  tree.remove(3)
  print(f"Removed 3")
  tree._print_tree()
  node = tree.lower_bound(3.1)
  assert node.get() == 4

  tree.remove(4)
  print(f"Removed 4")
  tree._print_tree()
  node = tree.lower_bound(4.1)
  assert node.get() == 6


def test_many_remove():
  for _ in range(100):
    data = list(range(5000))
    data_random = data[::]
    random.shuffle(data_random)
    tree = TreeMap()
    for d in data_random:
      tree[d] = d

    for pos, d in enumerate(data):
      tree.remove(d)
      lower_node = tree.lower_bound(d + 0.1)
      if pos == len(data) - 1:
        assert lower_node == tree.key_list_end()
      else:
        assert lower_node.get() == d + 1
