from typing import List

def shell_sort(numbers: List[int]) -> List[int]:
  len_numbers = len(numbers)
  gap = len_numbers // 2
  while gap > 0:
    for i in range(gap, len_numbers):
      tmp = numbers[i]
      j = i
      print(gap, end=" ")
      while j >= gap and numbers[j-gap] > tmp:
        numbers[j] = numbers[j-gap]
        j -= gap
      numbers[j] = tmp
    gap //= 2
  return numbers

if __name__ == '__main__':
  import random
  #nums = [random.randint(0, 1000) for _ in range(10)]
  nums = [5, 6, 9, 2, 3]
  print(shell_sort(nums))