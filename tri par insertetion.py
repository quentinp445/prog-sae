import numpy as np
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i-1
        while j >=0 and key_item < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key_item
    return arr
np.random.seed(1234)
t1 = np.random.randint(1, 45, size=5)
print("avant tri : ",t1)
t1 = insertion_sort(t1)
print("après tri : ",t1)
