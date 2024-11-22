from typing import List, Iterator, Tuple

def find_pair(pairs: List[Tuple[int, int]]) -> Iterator[Tuple[int, int]]:
  cache = {}
  for pair in pairs:
    first, second = pair[0],pair[1]
    value = cache.get(second)
    if not value:
      cache[first] = second
    elif value == first:
      yield pair

if __name__ == '__main__':
  pairs = [(1, 3), (2, 3), (1, 2), (3, 2)]
  for pair in find_pair(pairs):
    print(pair)