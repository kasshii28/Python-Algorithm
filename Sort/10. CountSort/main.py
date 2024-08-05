from typing import List

def count_sort(numbers: List[int]) -> List[int]:
  max_num = max(numbers)
  counts = [0]* (max_num + 1)
  result = [0]* len(numbers)

  for num in numbers:
    counts[num] += 1
  
  for i in range(1, len(counts)):
    counts[i] += counts[i-1]

  i = len(numbers) - 1
  while i >= 0:
    index = numbers[i]
    result[counts[index]-1] = numbers[i]
    counts[index] -=1
    i -= 1
  
  return result


if __name__ == '__main__':
  import random
  nums = [random.randint(0,1000) for _ in range(10)]
  #nums = [4,3,6,2,3,4,7]
  print(count_sort(nums))
