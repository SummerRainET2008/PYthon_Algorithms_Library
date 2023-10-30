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
  test_data = data[::]
  random.shuffle(test_data)
  for d in test_data:
    tree.set(d, d)

  for p in range(len(data)):
    lower_node = tree.lower_bound(data[p] + 0.1)
    if p == len(data) - 1:
      assert lower_node is None
    else:
      assert lower_node() == data[p + 1]

    lower_node = tree.lower_bound(data[p] - 0.1)
    assert lower_node() == data[p]

if __name__ == '__main__':
  nose.run(defaultTest=__name__)