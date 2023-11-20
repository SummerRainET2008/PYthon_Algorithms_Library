def search_KMP(text: str, pattern: str):
  def calc_suffix_array():
    ans = [-1] * len(pattern)
    for p in range(1, len(pattern)):
      prev_p = p - 1
      while prev_p != -1:
        if pattern[ans[prev_p] + 1] == pattern[p]:
          ans[p] = ans[prev_p] + 1
          break
        else:
          prev_p = ans[prev_p]

    return ans

  suffix_array = calc_suffix_array()
  p1 = 0
  p2 = -1
  while p1 < len(text) and p2 + 1 < len(pattern):
    if text[p1] == pattern[p2 + 1]:
      p1 += 1
      p2 += 1
    elif p2 != -1:
      p2 = suffix_array[p2]
    else:
      p1 += 1

  if p2 + 1 == len(pattern):
    return p1 - len(pattern)
  return -1


def search_mutipatterns(text: str, patterns: list):
  raise NotImplemented("todo")
