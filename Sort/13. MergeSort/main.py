from typing import List

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

if __name__ == "__main__":
  import random
  #nums = [random.randint(0, 1000) for _ in range(10)]
  nums = [5,4,1,8,7,3,2,9]
  print(merge_sort(nums))
