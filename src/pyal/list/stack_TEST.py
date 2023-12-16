'''
Author: Tian Xia (TianXia0209@gmail.com)
'''

from pyal.list.stack import Stack

def test_stack():
  stack = Stack()
  stack.push(1)
  stack.push(2)
  stack.push(3)
  assert stack.peek() == 3
  assert stack.pop() == 3

  stack.pop()
  stack.push(4)
  stack.pop()
  assert len(stack) == 1
  assert stack.pop() == 1
