def binary_search(arr, target):
    left = 0
    right = len(arr)
    
    while left < right:
        mid = (left+right)//2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = left + 1
        else:
            right = right - 1
    
    return -1