#coding: utf8
#author: Tian Xia

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
