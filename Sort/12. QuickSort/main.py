from typing import List

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


if __name__ == "__main__":
    import random
    #nums = [random.randint(0, 1000) for _ in range(10)]
    nums = [1,8,3,9,4,5,7]
    print(quick_sort(nums))