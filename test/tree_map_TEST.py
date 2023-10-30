from pyal.tree.tree_map import TreeMap
import nose
import random

def test_tree_construction():
  tree = TreeMap()
  random.seed(0)
  for _ in range(10):
    data = list(range(50))
    random.shuffle(data)
    print(f"test_tree_connstruction: {data=}")
    for d in data:
      tree.set(d, d)

    assert tree.size() == 50

    tree.set(0, 100)
    assert tree.get(0) == 100

def test_lower_bound():
  tree = TreeMap()
  data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  random.shuffle(data)
  for d in data:
    tree.set(d, d)

  lower_node = tree.lower_bound(4.5)
  print(f"lower_bound(4.5)={lower_node()}")
  assert lower_node() == 5

  lower_node = lower_node.next()
  print(f"lower_bound(5)={lower_node()}")
  assert lower_node() == 6


if __name__ == '__main__':
  nose.run(defaultTest=__name__)