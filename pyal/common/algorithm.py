'''
Author: Tian Xia (TianXia0209@gmail.com)
'''
import sys
import typing
import functools

INF = float("inf")
EPSILON = 1e-6

def is_none_or_empty(data) -> bool:
  '''This applies to any data type which has a __len__ method'''
  if data is None:
    return True

  try:
    return len(data) == 0
  except:
    return False

def histogram_ascii(points, out_file=sys.stdout) -> None:
  from collections import Counter
  import math

  counted = Counter(points)
  sumv = sum(counted.values())
  max_ratio = max([v / sumv for v in counted.values()] + [0])
  accum_sum = 0
  print(file=out_file)
  print(f"{'INDEX':>7} {'VALUE':>10} {'PERCENT':>7} {'ACCUM':>7}  {'FREQ'}",
        file=out_file)

  for index, [k, v] in enumerate(sorted(counted.items())):
    ratio = v / sumv
    tag = "*" if eq(max_ratio, ratio) else ""
    accum_sum += v
    bar_len = math.ceil(ratio / max_ratio * 120)
    key = f"{tag}{k}"
    percent1 = f"{ratio * 100:>5.2f}%"
    percent2 = f"{100 * accum_sum / sumv:>5.2f}%"
    print(
        f"{index:7d} {key:>10} {percent1:>7} {percent2:>7}  "
        f"{'+' * bar_len} {counted[k]}",
        file=out_file)

  print(file=out_file)


def is_sorted(data: list, strict: bool=False):
  if len(data) == 0:
    return True

  prev = data[0]
  for p in range(1, len(data)):
    if (strict and prev < data[p]) or (not strict and prev <= data[p]):
      prev = data[p]
    else:
      return False

  return True

def unique(data: list):
  '''
  :param data: must be sorted.
  '''
  def run():
    prev = None
    for d in data:
      if prev is None or d != prev:
        yield d
        prev = d

  return list(run())

def cmp(a, b) -> int:
  return (a > b) - (a < b)


def split_data_by_func(data: list, func):
  data1, data2 = [], []
  for d in data:
    if func(d):
      data1.append(d)
    else:
      data2.append(d)

  return data1, data2


def eq(v1, v2, prec=EPSILON):
  return abs(v1 - v2) < prec


def discrete_sample(dists: list) -> int:
  '''each probability must be greater than 0'''
  pass


def group_by_key_fun(data, key_fun=None):
  import collections
  '''
  data: list or dict
  Note, the spark.group_by_key requires the data is sorted by keys.
  @:return a dict
  '''
  result = collections.defaultdict(list)
  for d in data:
    key = d[0] if key_fun is None else key_fun(d)
    result[key].append(d)

  return result


def top_k(data: list, k: int, type="max", to_sort=False,
          data_key_func=lambda d: d):
  import heapq

  def top_k_largest(key_func):
    if len(data) <= k:
      return data

    min_heap = []
    for d in data:
      key = key_func(d)
      if len(min_heap) < k:
        heapq.heappush(min_heap, (key, d))
      elif key > min_heap[0][0]:
        heapq.heappop(min_heap)
        heapq.heappush(min_heap, (key, d))

    if to_sort:
      min_heap.sort(reverse=True)

    return [d for _, d in min_heap]

  if type == "max":
    return top_k_largest(data_key_func)
  elif type == "min":
    key_func = lambda item: -data_key_func(item)
    return top_k_largest(key_func)
  else:
    assert type in ["min", "max"]

def clamp(value, min_value, max_value):
  return min(max(value, min_value), max_value)

def argmax(data: list):
  if len(data) == 0:
    return -1

  opt_pos = 0
  for p in range(1, len(data)):
    if data[p] > data[opt_pos]:
      opt_pos = p

  return opt_pos

def argmin(data: list):
  if len(data) == 0:
    return -1

  opt_pos = 0
  for p in range(1, len(data)):
    if data[p] < data[opt_pos]:
      opt_pos = p

  return opt_pos

def make_new_list(shape: tuple, init_value):
  assert len(shape) > 0

  if len(shape) == 1:
    return [init_value for _ in range(shape[0])]

  return [make_new_list(shape[1:], init_value) for _ in range(shape[0])]

def swap(data: list, index1, index2):
  if index1 != index2:
    data[index1], data[index2] = data[index2], data[index1]

def rotate(data: list, middle: int, begin: int=0, end: int=None):
  '''
  :return: new list
  '''
  end = len(data) if end is None else end
  assert begin <= middle < end

  if middle == begin:
    return data[::]
  return data[: begin] + data[middle: end] + data[begin: middle]

def copy_to(src_list: list, begin: int, end: int,
            tgt_List: list, tgt_begin: int):
  size = end - begin
  tgt_List[tgt_begin: tgt_begin + size] = src_list[begin: end]

def the_kth_element(data: list, k_th: int, begin=0, end=None):
  import random
  end = len(data) if end is None else end
  assert 0 <= k_th < end - begin

  if end - begin == 1:
    return

  pos = random.randint(begin, end - 1)
  swap(data, pos, begin)
  pivot = data[begin]

  p1, p2 = begin, end - 1
  while p1 < p2:
    while p1 < p2:
      if not (pivot <= data[p2]):
        swap(data, p1, p2)
        p1 += 1
        break
      p2 -= 1
    else:
      break

    while p1 < p2:
      if not (data[p1] <= pivot):
        swap(data, p1, p2)
        p2 -= 1
        break
      p1 += 1
    else:
      break

  middle = p1
  status = cmp(middle - begin, k_th)
  if status == 0:
    return
  elif status < 0:
    the_kth_element(data, k_th - (middle - begin + 1), middle + 1, end)
  else:
    the_kth_element(data, k_th, begin, middle)

def lower_bound(data: list, target, begin: int=0, end: int=None):
  import bisect
  return bisect.bisect_left(
    data, target, begin, len(data) if end is None else end)

def upper_bound(data: list, target, begin: int=0, end: int=None):
  import bisect
  return bisect.bisect_right(
    data, target, begin, len(data) if end is None else end)

def reverse_in_place(data: list, begin: int, end: int=None):
  end = len(data) if end is None else end
  p1, p2 = begin, end - 1
  while p1 < p2:
    swap(data, p1, p2)
    p1 += 1
    p2 -= 1

def next_permutation(data: list):
  if is_none_or_empty(data):
    return []

  data = data[::]
  p = len(data) - 2
  while p >= 0 and data[p] >= data[p + 1]:
    p -= 1

  if p == -1:
    return data[::-1]

  reverse_in_place(data, p + 1, len(data))
  pos = upper_bound(data, data[p], p + 1)
  swap(data, p, pos)

  return data

def prev_permutation(data: list):
  pass

@functools.cache
def factorial(n: int):
  if n <= 1:
    return 1
  return n * factorial(n - 1)

'''
C(5, 3) = 5 * 4 * 3 / (3 * 2 * 1
'''
def combinatorial_number(n, k):
  if k > n - k:
    return combinatorial_number(n, n - k)

  ans = 1
  for p in range(k):
    ans *= (n - p) // (p + 1)

  return ans

def permutation_number(n, k):
  return combinatorial_number(n, k) * factorial(k)
