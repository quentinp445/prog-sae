import numpy as np

def binary_search_iterative(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

np.random.seed(1234)
t1 = np.random.randint(1, 45, size=5)
print("le loto donne ces 5 nombres aléatoires :")
print(t1)
t1.sort()
x = int(input("Entrez le nombre à rechercher :"))
result = binary_search_iterative(t1, x)
if result != -1:
    print("Le nombre", x, "a été trouvé à l'index", result)
else:
    print("Le nombre", x, "n'a pas été trouvé dans le tableau")
