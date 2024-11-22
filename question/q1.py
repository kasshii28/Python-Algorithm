from collections import Counter
from typing import List
import heapq

def top_n_with_heap(words: List[str], n: int)-> List[str]:
  # d = {}
  # for word in words:
  #   d[word] = d.get(word, 0) + 1
  # print(d)
  counter_word = Counter(words)
  data = [(-counter_word[word], word) for word in counter_word]
  heapq.heapify(data)
  return [heapq.heappop(data)[1] for _ in range(n)]

if __name__ == "__main__":
  w = ["python", "java","c","go","rust","python","go","c++","rust"]
  print(top_n_with_heap(w, 3))