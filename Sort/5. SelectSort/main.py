from typing import List

def select_sort(numbers: List[int]) -> List[int]:
  len_numbers = len(numbers)
  for i in range(len_numbers):
    min = i # 最小の値(仮)
    for j in range(i+1, len_numbers): # 最小以外の値の中から最小の値を見つける
      if numbers[min] > numbers[j]:
        min = j
    
    numbers[i], numbers[min] = numbers[min], numbers[i] #見つけた最小の値と交換

  return numbers


if __name__ == "__main__":
  import random
  nums = [random.randint(0, 1000) for i in range(10)]
  print(select_sort(nums))