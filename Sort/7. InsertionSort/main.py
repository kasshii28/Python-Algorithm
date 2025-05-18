from typing import List

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

if __name__ == '__main__':
  import random
  nums = [random.randint(0, 1000) for _ in range(10)]
  print(nums)
  print(insertion_sort(nums))