from pal.list import *

def display_list(list: LinkedList):
  iter = list.begin()
  while iter is not list.end():
    print(iter(), end=" ")
    iter = iter.next()
  print()

def main():
  list = LinkedList()

  list.push_back(1)
  list.push_back(2)
  list.push_back(3)
  list.push_back(4)
  display_list(list)

  list.insert_element(list.begin(), 100)
  iter = list.begin()
  print(iter())             # The first element is 100.

  last_element = list.pop_back()
  print(last_element)       # 4

  new_node = ListNode(0)
  list.insert(list.rbegin(), new_node)    # Insert into
  display_list(list)

if __name__ == "__main__":
  main()