'''
Author: Tian Xia (TianXia0209@gmail.com)
'''

from pyal.list.dequeue import Dequeue

def test_deque():
  dq = Dequeue()
  dq.push_front(1)
  dq.push_front(2)
  dq.push_back(3)
  dq.index(3) == dq.back()  # 2 1 3

  dq.pop_back()
  dq.pop_front()
  assert len(dq) == 1
  assert dq.front() == dq.back() == 1
