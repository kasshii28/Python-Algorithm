def binary_search(arr, target):
    left, right = 0, len(arr)-1
    
    while left <= right:
        print("右:",right)
        print("右の値:", arr[right])
        print("左:",left)
        print("左の値:", arr[left])
        mid = (left+right)//2
        print("中央:",mid)
        print("中央の値:", arr[mid])
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def remove_duplicates(arr):
    elements = []
    
    for item in arr:
        if item not in elements:
            elements.append(item)
    
    # return list(set(arr))
    return elements

def count_word(text):
    words = text.lower().split()
    word_count = {}
    
    for word in words:
        clean_word = ''.join(c for c in word if c.isalnum())
        
        if clean_word not in word_count:
            word_count[clean_word] = 1
        else:
            word_count[clean_word] += 1
    
    return word_count

def fact_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * fact_recursive(n-1)

def fact_iterative(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def fibo_recursive(n):
    if n <= 1:
        return n
    return fibo_recursive(n-1) + fibo_recursive(n-2)

def fibo_memo(n, memo={}):
    if n in memo:
        print("memo :", memo[n])
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibo_memo(n-1, memo) + fibo_memo(n-2, memo)
    print(memo[n])
    return memo[n]

if __name__ == '__main__':
    arr = [1,3,5,7,9,11,13,15,17,19]
    # binary_search(arr, 13)
    text = 'This is a sample text. This text is used for counting words. Sample it carefully.'
    # print(count_word(text))
    print(fibo_memo(25))