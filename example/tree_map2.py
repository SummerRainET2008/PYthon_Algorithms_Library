import pyal


def main():
  tree = pyal.TreeMap()

  tree[0] = "Hello"
  tree[1] = "World"
  tree[2] = "This"
  tree[3] = "is"
  tree[4] = "from"
  tree[5] = "pyal"
  tree[6] = "library"

  for key, value in tree.items():
    print(f"key={key}, value={value}")

  key_list_node = tree.key_list_begin()
  while key_list_node is not tree.key_list_end():
    print(f"key={key_list_node()}")
    key_list_node = key_list_node.next()

  lower_bound_node = tree.lower_bound(4.5)
  lower_bound_key = lower_bound_node()  # 5
  lower_bound_value = tree[lower_bound_key]  # pyal
  next_node = lower_bound_node.next()  # pointing to <6, library>
  print(next_node())

  upper_bound_node = tree.upper_bound(5)
  upper_bound_key = upper_bound_node()  # 6
  print(upper_bound_key)


if __name__ == "__main__":
  main()
