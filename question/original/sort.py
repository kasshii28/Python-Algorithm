class Sorts:
    def __init__(self, arr):
        self.arr = arr
    
    def selection_sort(self):
        arr = self.arr
        arr_len = len(arr)
        for i in range(arr_len):
            min = i
            for j in range(i+1, arr_len):
                if arr[min] > arr[j]:
                    min = j
            arr[i], arr[min] = arr[min], arr[i]
        return arr
if __name__ == '__main__':
    arr = [4,1,6,59,10,23,12,65,0,2,5,9,8]
    s = Sorts(arr)
    print(s.selection_sort())