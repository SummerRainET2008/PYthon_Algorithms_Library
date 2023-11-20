from pyal import search_KMP


def test_KMP():
  '''
  01234567890123456789
  abcabcdabcabcabcabcb
  '''
  pattern = "abcabcdabcabcabcabcb"
  text = "012abcabcdabcabcabcabcb012"
  assert search_KMP(text, pattern) == 3

  pattern = "abcabcabd"
  text = "abcabcabcabcabd"
  poses = "012345678901234"
  assert search_KMP(text, pattern) == 6
