from typing import Tuple
import operator
from collections import Counter

def most_count_char1(strings: str) -> Tuple[str, int]:
  # l = []
  # strings = strings.lower()
  # for char in strings:
  #   if not char.isspace():
  #     l.append((char, strings.count(char)))
  l = [(c, strings.count(c)) for c in strings if not c.isspace()]
  return max(l, key=operator.itemgetter(1))

def most_count_char2(strings: str) -> Tuple[str, int]:
  strings = strings.lower()
  hash = {}
  for char in strings:
    if not char.isspace():
      hash[char] = hash.get(char, 0) + 1
    max_key = max(hash, key=hash.get)
    return max_key, hash[max_key]

def most_count_char3(strings: str) -> Tuple[str, int]:
  strings = strings.lower()
  d = Counter()
  for char in strings:
    if not char.isspace():
      d[char] += 1
    max_key = max(hash, key=d.get)
    return max_key, d[max_key]

if __name__ == '__main__':
  s = 'This is a pen. This is an apple. Applepen'
  print(most_count_char1(s))