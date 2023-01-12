import numpy as np
def merge_sort_recursive(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort_recursive(left_half)
    right_half = merge_sort_recursive(right_half)
    return merge(left_half, right_half)
def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result
np.random.seed(1234)
t1 = np.random.randint(1, 45, size=5)
print("le loto donne ces 5 nombres aléatoires :")
print(t1)
t1 = merge_sort_recursive(t1)
print("les nombres triés par ordre croissant :")
print(t1)
