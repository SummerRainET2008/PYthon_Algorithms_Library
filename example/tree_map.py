import pyal

def main():
  tree_map = pyal.TreeMap()
  data = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e"), (5, "f")]
  for key, value in data:
    tree_map.set(key, value)

  key = 0
  print(f"{key=}, value={tree_map.get(key)=}")

  key = 1
  node = tree_map.lower_bound(key)
  print(f"lower_bound({key=}): {node()=}")
  print(f"upper_bound({key=}): {node.next()()=}")

  print(f"min key: {tree_map.key_list_begin()()}")
  print(f"max key: {tree_map.key_list_end().prev()()}")


if __name__ == "__main__":
  main()
