#coding: utf8
#author: Tian Xia

import os
import sys
import typing

INF = float("inf")
EPSILON = 1e-6

def load_module_from_full_path(path):
  import importlib.util
  path = os.path.abspath(path)
  spec = importlib.util.spec_from_file_location("module.name", location=path)
  foo = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(foo)
  return foo

def is_sys_mac():
  return sys.platform == "darwin"


def is_os_linux():
  return "linux" in sys.platform


def histogram_ascii(points, out_file=sys.stdout) -> None:
  from collections import Counter

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


def set_random_seeds(seed=0):
  '''
  :param seed: 0 means taking current time, or taking the seed value.
  '''
  if seed == 0:
    seed = os.getpid()
    Logger.info(f"current seed: {seed}")

  try:
    import torch
    torch.manual_seed(seed)
  except:
    Logger.error("failed to set random seeds")

  np.random.seed(seed)
  random.seed(seed)


def is_debugging():
  gettrace = getattr(sys, 'gettrace', None)
  if gettrace is None:
    return False
  else:
    return not is_none_or_empty(gettrace())


def next_batch(data: typing.Iterator, batch_size: int):
  _ = range(batch_size)
  data_iter = iter(data)
  while True:
    buff = list(zip(_, data_iter))
    if buff == []:
      break
    batch_data = list(map(itemgetter(1), buff))
    yield batch_data


def ensure_random_seed_for_one_time(buff={}):
  key = "randomized"
  status = buff.get(key, False)
  if not status:
    random.seed()
    buff[key] = True


def get_new_temporay_file():
  return tempfile.NamedTemporaryFile(delete=False).name


def next_line_from_file(file_name: str, max_count: int = -1):
  for idx, ln in enumerate(open(file_name)):
    if (max_count > 0 and idx < max_count) or max_count <= 0:
      yield ln.rstrip()


def next_line_from_file_list(file_names: list, max_count: int = -1):
  for f in file_names:
    yield from next_line_from_file(f, max_count)


def is_sorted(data: list):
  pass

def uniq(data: list) -> typing.Iterator:
  '''
  :param data: must be sorted.
  '''
  prev = None
  for d in data:
    if prev is None or d != prev:
      yield d
      prev = d

def norm1(vec):
  vec = np.array(vec)
  nm = float(sum(abs(vec)))
  return vec if eq(nm, 0) else vec / nm


def norm2(vec):
  vec = np.array(vec)
  nm = math.sqrt(sum(vec * vec))
  return vec if eq(nm, EPSILON) else vec / nm


def cmp(a, b) -> int:
  return (a > b) - (a < b)


def get_home_dir():
  return os.environ["HOME"]


def mkdir(folder: str, delete_first: bool=False) -> None:
  # create folder recursively.
  if delete_first:
    execute_cmd(f"rm -r {folder}")

  path = "/" if folder.startswith("/") else ""
  for subfolder in folder.split("/"):
    path = os.path.join(path, subfolder)
    if not os.path.exists(path):
      execute_cmd(f"mkdir {path}")


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


def get_files_in_folder(data_path,
                        file_extensions: typing.Union[list, set] = None,
                        resursive=False) -> list:
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

  for path, folders, files in os.walk(data_path,
                                      topdown=resursive,
                                      followlinks=False):
    for short_name in files:
      if legal_file(short_name):
        yield os.path.realpath(os.path.join(path, short_name))


def split_data_by_func(data, func):
  data1, data2 = [], []
  for d in data:
    if func(d):
      data1.append(d)
    else:
      data2.append(d)
  return data1, data2


def is_none_or_empty(data) -> bool:
  '''This applies to any data type which has a __len__ method'''
  if data is None:
    return True

  try:
    return len(data) == 0
  except:
    return False


def __strdate(timezone: str, now):
  city = timezone.split("/")[-1]
  ts = now.strftime("%Y-%m-%d_%Ih-%Mm-%Ss_%p")
  return f"{city}_{ts}"


def command(cmd: str,
            capture_output: bool = False,
            server=None,
            account=None,
            buff={}):
  '''return (status_code, stdout, stderror)'''
  current_IPs = buff.setdefault(
      "current_IP",
      set([
          attr[0].address for net_name, attr in psutil.net_if_addrs().items()
      ]))
  if server == "127.0.0.1" or server is None or server in current_IPs:
    full_cmd = cmd
  else:
    assert "'" not in cmd
    if account is None:
      account = os.getlogin()
    full_cmd = f"ssh -oStrictHostKeyChecking=no {account}@{server} '{cmd}'"

  Logger.debug(f"[start] executing '{full_cmd}'")
  result = subprocess.run(full_cmd, shell=True, capture_output=capture_output)
  status = "OK" if result.returncode == 0 else "fail"
  Logger.debug(f"[finish - {status}] '{full_cmd}'")

  if capture_output:
    return result.returncode, result.stdout.decode(), result.stderr.decode()
  else:
    return result.returncode, "", ""


def eq(v1, v2, prec=EPSILON):
  return abs(v1 - v2) < prec


def discrete_sample(dists) -> int:
  '''each probability must be greater than 0'''
  dists = np.array(dists)
  assert all(dists >= 0)
  accsum = scipy.cumsum(dists)
  expNum = accsum[-1] * random.random()
  return bisect.bisect(accsum, expNum)


def group_by_key_fun(data, key_fun=None):
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


def is_wide_char(ch):
  return unicodedata.east_asian_width(ch) in ['W', "F"]


def get_console_text_length(text):
  ext_len = sum([is_wide_char(e) for e in text])
  return len(text) + ext_len


def full_justify_zh_en(article: str, max_width) -> list:
  def split(text):
    text = text.strip()
    console_len_sum = 0
    for p, e in enumerate(text):
      console_len_sum += 1
      if is_wide_char(e):
        console_len_sum += 1

      # print(f"{console_len_sum}, {p}, '{e}', {char_type}, {text[: p + 1]}")

      if console_len_sum == max_width:
        return text[:p + 1], text[p + 1:]
      elif console_len_sum == max_width + 1:
        return text[:p], text[p:]

    return text, ""

  article = " ".join(article.split())
  ret = []
  remaining = article
  while remaining != "":
    text, remaining = split(remaining)
    ret.append(text)

  return ret


def full_justify_en(article: str, max_width) -> list:
  words = article.split()
  buff, words_length = [], 0
  ret, p = [], 0
  while p < len(words):
    w = words[p]
    if words_length + len(w) + len(buff) <= max_width:
      buff.append(w)
      if p == len(words) - 1:
        ret.append(" ".join(buff))
      else:
        words_length += len(w)
      p += 1
    elif buff == []:
      assert words_length == 0
      ret.append(w)
      p += 1
    else:
      if len(buff) == 1:
        ret.append(buff[0].rjust(max_width))
      else:
        blank = (max_width - words_length) // (len(buff) - 1)
        mod = max_width - words_length - blank * (len(buff) - 1)
        ret.append((" " * (blank + 1)).join(buff[:mod + 1]) + " " * blank +
                   (" " * blank).join(buff[mod + 1:]))
      buff = []
      words_length = 0

  return ret


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

def top_k_max_or_min(data: list,
                     k,
                     type="max",
                     to_sort=False,
                     data_key_func=lambda d: d):
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
