from typing import List

def Bubble_sort(numbers: List[int]) -> List[int]:
  len_numbers = len(numbers)
  for i in range(len_numbers):
    print(len_numbers-i-1)
    for j in range(len_numbers-i-1):
      if numbers[j] > numbers[j+1]:
        numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
  return numbers

def select_sort(numbers: List[int]) -> List[int]:
  len_numbers = len(numbers)
  for i in range(len_numbers):
    min = i # 最小の値(仮)
    for j in range(i+1, len_numbers): # 最小以外の値の中から最小の値を見つける
      if numbers[min] > numbers[j]:
        min = j
    
    numbers[i], numbers[min] = numbers[min], numbers[i] #見つけた最小の値と交換

  return numbers

def insertion_sort(numbers: List[int]) -> List[int]:
  len_numbers = len(numbers)
  for i in range(1, len_numbers):
    tmp = numbers[i] # 未ソート部分の先頭の値
    j = i - 1 # ソート済みの最後尾
    print("tmp: ",tmp, "j: ",j)
    while j >= 0 and numbers[j] > tmp: # jが配列のindex内かつ配列[j]の値がtmpより大きい場合ループ
      print("j+1: ", numbers[j+1], "j: ",numbers[j])
      numbers[j+1] = numbers[j] # tmpの値の位置と入れ替え
      j -= 1 # ソート済みのindexを下げていく
    
    numbers[j+1] = tmp # ソート済みの先頭の値に最小の値を入れる
    print(numbers[j+1], tmp)

  return numbers

def merge_sort(numbers: List[int]):
  print(numbers)
  if len(numbers) <= 1:
    return numbers

  mid = len(numbers) // 2
  left = merge_sort(numbers[:mid])
  right = merge_sort(numbers[mid:])
  print("左:",left, "右:",right)

  return merge(left,right)

def merge(left, right):
  res = []
  i=j=0
  
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      res.append(left[i])
      i+=1
    else:
      res.append(right[j])
      j+=1
    
  res.extend(left[i:])
  res.extend(right[j:])
  
  print("マージ済み",res)
  return res

def partition(numbers: List[int], low: int, high: int) -> int:
    i = low-1
    pivot = numbers[high]
    for j in range(low, high):
        if numbers[j] <= pivot:
            i+=1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
    return i+1

def quick_sort(numbers: List[int]) -> List[int]:
    def _quick_sort(numbers: List[int], low: int, high: int) -> None:
        if low < high:
          par_index = partition(numbers, low, high)
          _quick_sort(numbers, low, par_index-1)
          _quick_sort(numbers, par_index+1, high)
    
    _quick_sort(numbers, 0, len(numbers) - 1)
    return numbers

def bucket_sort(numbers: List[int]) -> List[int]:
  max_num = max(numbers)
  len_numbers = len(numbers)
  size = max_num // len_numbers

  buckets = [[] for _ in range(size)]
  for num in numbers:
    i = num // size
    if i!= size:
      buckets[i].append(num)
    else:
      buckets[size-1].append(num)
  
  for i in range(size):
    insertion_sort(buckets[i])

  result = []
  for i in range(size):
    result += buckets[i]
  
  return result