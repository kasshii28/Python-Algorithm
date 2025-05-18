from typing import List

def Bubble_sort(numbers: List[int]) -> List[int]:
  len_numbers = len(numbers)
  for i in range(len_numbers):
    print(len_numbers-i-1)
    for j in range(len_numbers-i-1):
      if numbers[j] > numbers[j+1]:
        numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
  return numbers


if __name__ == '__main__':
  import random
  nums = [random.randint(0, 1000) for i in range(10)]
  print(Bubble_sort(nums))