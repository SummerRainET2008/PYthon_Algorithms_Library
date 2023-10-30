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

if __name__ == '__main__':
  nose.run(defaultTest=__name__)