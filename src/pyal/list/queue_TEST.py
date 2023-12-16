'''
Author: Tian Xia (TianXia0209@gmail.com)
'''

from pyal.list.queue import Queue

def test_queue():
  queue = Queue()
  queue.push(1)
  queue.push(2)
  assert queue.peek() == 1
  assert queue.pop() == 1
  assert queue.pop() == 2
  assert len(queue) == 0


