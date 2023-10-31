'''
Author: Tian Xia (TianXia0209@gmail.com)
'''

import sys
import typing

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

def unique(data: list) -> typing.Iterator:
  '''
  :param data: must be sorted.
  '''
  prev = None
  for d in data:
    if prev is None or d != prev:
      yield d
      prev = d

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
    if data[p] < data[opt_pos]:
      opt_pos = p

  return opt_pos

def make_nd_list(shape: tuple, init_value):
  assert len(shape) > 0

  if len(shape) == 1:
    return [init_value for _ in range(shape[0])]

  return [make_nd_list(shape[1:]) for _ in range(shape[0])]

def remove_if(data: list, cond):
  pass

def replace_if(data: list, cond):
  pass

def swap(data: list, index1, index2):
  if index1 != index2:
    data[index1], data[index2] = data[index2], data[index1]

def rotate(data: list, middle: int, first=0, last=None):
  pass

def nth_element(data: list, n_th: int, first=0, last=None):
  pass

def lower_bound(data: list, first: int, last: int):
  pass

def upper_bound(data: list, first: int, last: int):
  pass

def next_permutation(data: list):
  pass

def prev_permutation(data: list):
  pass

