'''
Author: Tian Xia (TianXia0209@gmail.com)
'''
import copy
import math
from operator import itemgetter
import datetime
import functools
import importlib.util
import importlib
import os
import psutil
import pytz
import random
import re
import socket
import subprocess
import sys
import tempfile
import threading
import time
import json
import typing
from typing import Union, List, Iterator
from threading import Thread
import queue

INF = math.inf
EPSILON = 1e-6

def read_file_content(file_name: str, mode="r"):
  with open(file_name, mode) as fin:
    return fin.read().strip()

def read_file_lines(file_name: str, mode="r"):
  with open(file_name, mode) as fin:
    for ln in fin:
      yield ln.rstrip()

def load_py_data(py_file):
  user_data = {}
  with open(py_file) as fin:
    try:
      exec(compile(fin.read(), "py_data", "exec"), user_data)
      return user_data
    except Exception as error:
      Logger.error(error)
      return {}


def load_module_from_full_path(path):
  path = os.path.abspath(path)
  spec = importlib.util.spec_from_file_location("module.name", location=path)
  foo = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(foo)
  return foo


def async_function(f):
  '''
  Decorator
  :param f: a function with no return value.
  :return: a threading.Thread

  You should call threading.Thread.join() after calling f.
  '''
  def wrapper(*args, **kwargs):
    thr = threading.Thread(target=f, args=args, kwargs=kwargs)
    thr.start()
    return thr

  return wrapper


def is_sys_mac():
  return sys.platform == "darwin"


def is_os_linux():
  return "linux" in sys.platform


def is_debugging():
  gettrace = getattr(sys, 'gettrace', None)
  if gettrace is None:
    return False
  else:
    return not is_none_or_empty(gettrace())


def get_new_temporay_file():
  return tempfile.NamedTemporaryFile(delete=False).name


def next_line_from_file(file_name: str, max_count: int = -1):
  for idx, ln in enumerate(open(file_name)):
    if (max_count > 0 and idx < max_count) or max_count <= 0:
      yield ln.rstrip()


def next_line_from_files(file_names: list, max_count: int = -1):
  for f in file_names:
    yield from next_line_from_file(f, max_count)


def segment_contain(seg1: list, seg2: list):
  if seg1[0] <= seg2[0] and seg2[1] <= seg1[1]:
    return 1
  if seg2[0] <= seg1[0] and seg1[1] <= seg2[1]:
    return -1
  return 0


def segment_intersec(seg1: list, seg2: list):
  return not segment_no_touch(seg1, seg2)


def segment_no_touch(seg1: list, seg2: list):
  return seg1[1] <= seg2[0] or seg2[1] <= seg1[0]


def get_home_dir():
  return os.environ["HOME"]


def mkdir(folder: str, delete_first: bool = False) -> None:
  # create folder recursively.
  if delete_first:
    command(f"rm -r {folder}")

  path = "/" if folder.startswith("/") else ""
  for subfolder in folder.split("/"):
    path = os.path.join(path, subfolder)
    if not os.path.exists(path):
      command(f"mkdir {path}")


def get_module_path(module_name) -> typing.Union[str, None]:
  '''
  This applys for use-defined moudules.
  e.g., get_module_path("NLP.translation.Translate")
  '''
  module_name = module_name.replace(".", "/") + ".py"
  for path in sys.path:
    path = path.strip()
    if path == "":
      path = os.getcwd()

    file_name = os.path.join(path, module_name)
    if os.path.exists(file_name):
      return path

  return None


def csv_file_read(file_name, max_num: int=-1)-> typing.Iterator:
  import csv
  assert file_name.endswith(".csv")
  data_num = 0
  with open(file_name, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      data_num += 1
      if max_num >= 0 and data_num > max_num:
        break

      if data_num > 0 and data_num % 10_000 == 0:
        Logger.info(f"{file_name}: {data_num} lines have been loaded.")

      yield row

  Logger.info(f"{file_name}: #data={data_num:,}")

def csv_file_write(data: typing.Iterator, field_names: list,
                   file_name, remove_extra_keys=True, **kwargs):
  assert file_name.endswith(".csv")
  import csv
  with open(file_name, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    for d in data:
      if remove_extra_keys:
        d = d.copy()
        for k in list(d.keys()):
          if k not in field_names:
            del d[k]

      writer.writerow(d)


def pydict_file_read(file_name, max_num: int = -1) -> typing.Iterator:
  assert file_name.endswith(".pydict")
  data_num = 0
  with open(file_name, encoding="utf-8") as fin:
    for idx, ln in enumerate(fin):
      if max_num >= 0 and idx + 1 > max_num:
        break
      if idx > 0 and idx % 10_000 == 0:
        Logger.info(f"{file_name}: {idx} lines have been loaded.")

      try:
        obj = eval(ln)
        yield obj
        data_num += 1

      except Exception as err:
        Logger.error(f"reading {file_name}:{idx + 1}: {err} '{ln}'")

  Logger.info(f"{file_name}: #data={data_num:,}")


def json_file_write(data, file_name: str):
  if isinstance(data, dict):
    json_data = data
  else:
    json_data = {"data": data}

  with open(file_name, "w") as fout:
    json_formatted_str = json.dumps(json_data, indent=2)
    fout.write(json_formatted_str)


def json_file_load(file_name: str):
  with open(file_name) as fin:
    config = json.load(fin)
    return config


def pydict_file_write(data: typing.Iterator, file_name: str, **kwargs) -> None:
  assert file_name.endswith(".pydict")
  if isinstance(data, dict):
    data = [data]
  with open(file_name, "w") as fou:
    num = 0
    for obj in data:
      num += 1
      obj_str = str(obj)
      if "\n" in obj_str:
        Logger.error(f"pydict_file_write: not '\\n' is allowed: '{obj_str}'")
      print(obj, file=fou)
      if kwargs.get("print_log", True) and num % 10_000 == 0:
        Logger.info(f"{file_name} has been written {num} lines")
      if kwargs.get("flush_freq", None) is not None and \
        num % kwargs["flush_freq"] == 0:
        fou.flush()

  if kwargs.get("print_log", True):
    Logger.info(f"{file_name} has been written {num} lines totally")


def get_file_extension(file_name: str) -> str:
  return file_name.split(".")[-1]


def replace_file_name(file_name: str, old_suffix: str, new_suffix: str):
  assert old_suffix in file_name
  return file_name[:len(file_name) - len(old_suffix)] + new_suffix


def get_files_in_folder(data_path,
                        file_extensions: typing.Union[list, set] = None,
                        recursive=False) -> list:
  '''file_exts: should be a set, or None, e.g, ["wav", "flac"]
  return: a list, [fullFilePath]'''
  def legal_file(short_name):
    if short_name.startswith("."):
      return False
    ext = get_file_extension(short_name)
    return is_none_or_empty(file_extensions) or ext in file_extensions

  if file_extensions is not None:
    assert isinstance(file_extensions, (list, set))
    file_extensions = set(file_extensions)

  all_folders = set()
  for path, folders, files in os.walk(data_path,
                                      topdown=True,
                                      followlinks=False):
    if not recursive:
      for folder in folders:
        all_folders.add(os.path.join(path, folder))
      if path in all_folders:
        continue

    for short_name in files:
      if legal_file(short_name):
        yield os.path.realpath(os.path.join(path, short_name))


def to_readable_time(seconds: float):
  if seconds < 0:
    return f"negative time: {seconds} seconds."
  if seconds >= 365 * 24 * 3600:
    return "over 365 days"

  n_day = int(seconds / (24 * 3600))
  n_hour = int((seconds - n_day * 24 * 3600) / 3600)
  n_min = int((seconds - n_day * 24 * 3600 - n_hour * 3600) / 60)
  n_sec = seconds - n_day * 24 * 3600 - n_hour * 3600 - n_min * 60

  result = []
  if n_day > 0:
    result.append(f"{n_day} d")
  if n_hour > 0:
    result.append(f"{n_hour} h")
  if n_min > 0:
    result.append(f"{n_min} m")
  if n_sec > 0:
    result.append(f"{n_sec:.3f} s")

  return " ".join(result)


def __strdate(timezone: str, now):
  city = timezone.split("/")[-1]
  ts = now.strftime("%Y-%m-%d_%Ih-%Mm-%Ss_%p")
  return f"{city}_{ts}"


def get_log_time(utc_time: bool = True, country_city: str = None):
  '''
  utc_time: if False, return local time(server);
            if True, return local time(city).
  country_city : When utc_time is true,  if city is None, return UTC(0).
                See pytz/__init__.py:510, all_timezones

  e.g., SF time is UTC+8, then get_log_time(True) - 8 = get_log_time(False)
  '''
  if utc_time:
    if is_none_or_empty(country_city):
      now = datetime.datetime.utcnow()
      return __strdate("utc", now)
    else:
      now = datetime.datetime.now(pytz.timezone(country_city))
      return __strdate(country_city, now)

  else:
    now = datetime.datetime.now()
    return __strdate("local", now)


def get_future_time(days=0,
                    hours=0,
                    minutes=0,
                    seconds=0,
                    country_city: str = None):
  delta = datetime.timedelta(days=days,
                             hours=hours,
                             minutes=minutes,
                             seconds=seconds)
  if is_none_or_empty(country_city):
    finished_time = datetime.datetime.now() + delta
    return __strdate("utc", finished_time)
  else:
    finished_time = datetime.datetime.now(pytz.timezone(country_city)) + delta
    return __strdate(country_city, finished_time)


@functools.lru_cache
def get_IPs():
  return set(
      [attr[0].address for net_name, attr in psutil.net_if_addrs().items()])


@functools.lru_cache
def get_server_ip():
  """
  modify by xuan, 2022-11-3
  """
  hostname = socket.gethostname()
  local_ip = socket.gethostbyname(hostname)
  return local_ip


@functools.lru_cache
def get_server_ip0():
  st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  try:
    st.connect(('10.255.255.255', 1))
    ip = st.getsockname()[0]
  except Exception:
    ip = '127.0.0.1'
  finally:
    st.close()

  return ip


def command(cmd: str,
            capture_output: bool = False,
            server_ip=None,
            account=None,
            buff={}):
  '''return (status_code, stdout, stderror)'''

  current_IPs = get_IPs()
  if server_ip == "127.0.0.1" or server_ip is None or server_ip in current_IPs:
    full_cmd = cmd
  else:
    assert "'" not in cmd
    if account is None:
      account = os.getlogin()
    full_cmd = f"ssh -oStrictHostKeyChecking=no {account}@{server_ip} '{cmd}'"

  Logger.debug(f"[start] executing '{full_cmd}'")
  result = subprocess.run(full_cmd, shell=True, capture_output=capture_output)
  status = "OK" if result.returncode == 0 else "fail"
  Logger.debug(f"[finish - {status}] '{full_cmd}'")

  if capture_output:
    return result.returncode, result.stdout.decode(), result.stderr.decode()
  else:
    return result.returncode, "", ""


def to_utf8(line) -> typing.Union[str, None]:
  if type(line) is str:
    try:
      return line.encode("utf8")
    except:
      Logger.warn("in toUtf8(...)")
      return None

  elif type(line) is bytes:
    return line

  Logger.error("wrong type in toUtf8(...)")
  return None


def print_flush(cont, stream=None) -> None:
  if stream is None:
    stream = sys.stdout
  print(cont, file=stream)
  stream.flush()


def display_server_info():
  host_name = socket.gethostname()
  ip = get_server_ip()
  Logger.info(f"server information: {host_name}({ip}), process: {os.getpid()}")


def get_available_gpus(server_ip=None, account=None):
  def find():
    memory_regex = r'([0-9]+)MiB / .* Default'

    res = command("nvidia-smi",
                  capture_output=True,
                  server_ip=server_ip,
                  account=account)[1]
    Logger.debug(f"server: {server_ip}, {res}")
    res = res.split("\n")
    if len(res) <= 6:
      Logger.error(
          f"can not obtain correct nvidia-smi result: {' '.join(res)}")
      yield -1
      return

    gpu_num = 0
    for row in res:
      info = re.findall(memory_regex, row)
      if info != []:
        gpu_num += 1

        memory = int(info[0])
        if memory < 512:
          yield gpu_num - 1

  def find_all():
    return list(find())

  try:
    ret = timeout(find_all, [], 30)
    return ret
  except TimeoutError:
    Logger.error(f"Time out: get_available_gpus({server_ip})")
    return []
  except Exception as error:
    Logger.error(error)
    return []


def timeout(func, args: list, max_time_seconds):
  class _MonitorThread(threading.Thread):
    def __init__(self, ret: list):
      threading.Thread.__init__(self, daemon=True)
      self._ret = ret

    def run(self):
      if args == []:
        ret = func()
      else:
        ret = func(*args)
      self._ret.append(ret)

  status = []
  _MonitorThread(status).start()

  total_millionseconds = int(max_time_seconds * 1000)
  step = min(total_millionseconds, 100)
  for _ in range(0, total_millionseconds, step):
    time.sleep(step / 1000)
    if status != []:
      return status[0]

  raise TimeoutError()


class Timer(object):
  def __init__(self, title="") -> None:
    self.title = title
    self.__starting = None
    self.__duration = None

  @property
  def duration(self):
    if self.__duration is not None:
      return self.__duration
    elif self.__starting is None:
      return 0
    else:
      return time.time() - self.__starting

  def __enter__(self) -> None:
    if not is_none_or_empty(self.title):
      Logger.info(f"Timer starts:\t '{self.title}'")
    self.__starting = time.time()
    return self

  def __exit__(self, *args) -> None:
    self.__duration = time.time() - self.__starting
    if not is_none_or_empty(self.title):
      Logger.info(
          f"Timer finishes:\t '{self.title}', takes {to_readable_time(self.duration)} "
          f"seconds.")


class Logger:
  '''
  debug=0, info=1, warning=2, error=3
  '''
  level = 1
  outstream = sys.stdout
  country_city = ""  #"Asia/Chongqing", 'America/Los_Angeles'

  @staticmethod
  def reset_outstream(out_file: str, append=False):
    mode = "a" if append else "w"
    Logger.outstream = open(out_file, mode)

  @staticmethod
  def set_level(level):
    Logger.level = level

  @staticmethod
  def is_debug():
    return Logger.level <= 0

  @staticmethod
  def debug(*args):
    if Logger.level <= 0:
      print(get_log_time(country_city=Logger.country_city),
            "DEBUG:",
            *args,
            file=Logger.outstream)
      Logger.outstream.flush()

  @staticmethod
  def info(*args):
    if Logger.level <= 1:
      print(get_log_time(country_city=Logger.country_city),
            "INFO:",
            *args,
            file=Logger.outstream)
      Logger.outstream.flush()

  @staticmethod
  def warn(*args):
    if Logger.level <= 2:
      print(get_log_time(country_city=Logger.country_city),
            "WARN:",
            *args,
            file=Logger.outstream)
      Logger.outstream.flush()

  @staticmethod
  def error(*args):
    if Logger.level <= 3:
      print(get_log_time(country_city=Logger.country_city),
            "ERR:",
            *args,
            file=Logger.outstream)
      Logger.outstream.flush()


def bit_not(m):
  import ctypes
  return ctypes.c_uint32(~m).value


@functools.lru_cache
def ensure_random_seed_for_one_time():
  random.seed()


def next_batch(data: typing.Iterator, batch_size: int):
  _ = range(batch_size)
  data_iter = iter(data)
  while True:
    buff = list(zip(_, data_iter))
    if buff == []:
      break
    batch_data = list(map(itemgetter(1), buff))
    yield batch_data


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


def is_sorted(data: list, strict: bool = False):
  if len(data) <= 1:
    return True

  for p in range(1, len(data)):
    if not ((strict and data[p - 1] < data[p]) or
            (not strict and data[p - 1] <= data[p])):
      break
  else:
    return True

  for p in range(1, len(data)):
    if not ((strict and data[p - 1] > data[p]) or
            (not strict and data[p - 1] >= data[p])):
      break
  else:
    return True

  return False


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


def unique_in_place(nums: list):
  p1 = 0
  for p2 in range(1, len(nums)):
    if nums[p2] == nums[p1]:
      continue

    p1 += 1
    nums[p1] = nums[p2]

  return p1 + 1


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


def discrete_sample(probs: list) -> int:
  '''each probability must be greater than 0'''
  from itertools import accumulate
  import random
  aprobs = list(accumulate(probs))
  assert eq(aprobs[-1], 1.0)
  rand_prob = random.random()
  for pos, prob in enumerate(aprobs):
    if rand_prob <= prob:
      return pos


"""def group_by_key_fun(data, key_fun=None):
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

  return result"""


def top_n(data: list,
          n_num: int,
          type="max",
          to_sort=False,
          data_key_func=lambda d: d):
  assert type in ["min", "max"]
  assert 1 <= n_num <= len(data)

  data = [(data_key_func(d), d) for d in data]
  if type == "max":
    k_th = len(data) - n_num - 1
    kth_smallest_element(data, k_th)
    ans = [v for _, v in data[k_th + 1:]]
    return sorted(ans, reverse=True) if to_sort else ans
  else:
    k_th = n_num - 1
    kth_smallest_element(data, k_th)
    ans = [v for _, v in data[:k_th + 1]]
    return sorted(ans, reverse=False) if to_sort else ans


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


def make_list(shape: tuple, init_value: typing.Any):
  assert len(shape) > 0

  if len(shape) == 1:
    if init_value is None or isinstance(init_value, (int, float, str)):
      return [init_value] * shape[0]
    else:
      return [copy.deepcopy(init_value) for _ in range(shape[0])]

  return [make_list(shape[1:], init_value) for _ in range(shape[0])]


def swap(data: list, index1, index2):
  if index1 != index2:
    data[index1], data[index2] = data[index2], data[index1]


def rotate(data: list, middle: int, begin: int = 0, end: int = None):
  '''
  :return: new list
  '''
  end = len(data) if end is None else end
  assert begin <= middle < end

  if middle == begin:
    return data[::]
  return data[:begin] + data[middle:end] + data[begin:middle]


def copy_to(src_list: list, begin: int, end: int, tgt_List: list,
            tgt_begin: int):
  size = end - begin
  tgt_List[tgt_begin:tgt_begin + size] = src_list[begin:end]


def kth_smallest_element(data: list, k_th: int, begin=0, end=None):
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
    kth_smallest_element(data, k_th - (middle - begin + 1), middle + 1, end)
  else:
    kth_smallest_element(data, k_th, begin, middle)


def lower_bound(data: list, target, begin: int = 0, end: int = None):
  import bisect
  return bisect.bisect_left(data, target, begin,
                            len(data) if end is None else end)


def upper_bound(data: list, target, begin: int = 0, end: int = None):
  import bisect
  return bisect.bisect_right(data, target, begin,
                             len(data) if end is None else end)


def reverse_in_place(data: list, begin: int, end: int = None):
  end = len(data) if end is None else end
  data[begin:end] = data[begin:end][::-1]


def sort_in_place(data: list, reverse=False, begin: int = 0, end: int = None):
  end = len(data) if end is None else end
  data[begin:end] = sorted(data[begin:end], reverse=reverse)


def find_first_if(data: list, predicate, begin: int = 0, end: int = None):
  end = len(data) if end is None else end
  p = begin
  while p < end:
    if predicate(data[p]):
      return p
    p += 1
  return -1


def find_last_if(data: list, predicate, begin: int = 0, end: int = None):
  end = len(data) if end is None else end
  p = end - 1
  while p >= begin:
    if predicate(data[p]):
      return p
    p -= 1
  return -1


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
  raise NotImplemented("todo")


@functools.lru_cache
def factorial(n: int):
  if n <= 1:
    return 1
  return n * factorial(n - 1)


@functools.lru_cache
def combinatorial_number(n, k):
  if k > n - k:
    return combinatorial_number(n, n - k)

  ans = 1
  for p in range(k):
    ans *= (n - p) // (p + 1)

  return ans


@functools.lru_cache
def permutation_number(n, k):
  return combinatorial_number(n, k) * factorial(k)


def combinations_with_duplicate(data: list, k: int) -> iter:
  '''
  :param data: should be sortable.
  :return:
  '''
  @functools.lru_cache
  def _comb_helper(start, _k):
    # print(f"debug: {start=} {_k=}")
    if not (len(sdata) - start >= _k):
      return []

    if _k == 0:
      return [[]]

    else:
      last_p = None
      solus = []
      for cur_p in range(start, len(sdata)):
        if last_p is None or sdata[last_p] != sdata[cur_p]:
          last_p = cur_p
          for solu in _comb_helper(cur_p + 1, _k - 1):
            solus.append([sdata[cur_p]] + solu)

      # print(f"{start=}, {_k=}: {solus=}")
      return solus

  # _comb_helper.cache_clear()

  sdata = sorted(data)
  yield from _comb_helper(0, k)


def group_data(data: list, sequential: bool = True) -> iter:
  '''
  :param data: list
  :param sequential: if True then data is like [1, 1, 2, 2, 0, 0, 0]; otherwise
  the data is like [1, 0, 2, 2, 1, 0, 0]
  :return: iterator
  '''
  if data == []:
    return

  if sequential:
    e, freq = None, 0
    for v in data:
      if e is None:
        e, freq = v, 1
      elif v == e:
        freq += 1
      else:
        yield (e, freq)
        e, freq = v, 1

    yield (e, freq)

  elif isinstance(data[0], (int, float, str)):
    from collections import Counter
    counter = Counter(data)
    for k, f in counter.items():
      yield k, f

  else:
    data = sorted(data)
    yield from group_data(data, sequential=True)

class Pool:
  def __init__(self, processes=4):
    self._worker_num = processes

  def map(self, user_func, args_list: Union[List, Iterator])-> Iterator:
    def _thread_worker(index_queue: queue.Queue, out_queue: queue.Queue):
      while True:
        data_id = index_queue.get()
        if not (data_id < len(args_list)):
          break

        result = user_func(*args_list[data_id])
        out_queue.put((data_id, result))

    args_list = list(args_list)
    index_queue = queue.Queue()
    for idx in range(len(args_list) + self._worker_num):
      index_queue.put(idx)

    out_queue = queue.Queue()
    threads = [Thread(target=_thread_worker, args=(index_queue, out_queue))
               for _ in range(self._worker_num)]
    for td in threads:
      td.start()

    results = {}
    cur_index = 0
    while cur_index < len(args_list):
      index, resp = out_queue.get()
      results[index] = resp

      while cur_index in results:
        yield results[cur_index]
        del results[cur_index]
        cur_index += 1
