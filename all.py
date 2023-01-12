import numpy as np
import matplotlib.pyplot as plt


def merge_sort_recursive(arr): #tri fusion
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

def cocktail_sort(arr): # tri cocktail
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):
        swapped = False
        for i in range(start, end):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if (swapped == False):
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start = start + 1
    return arr

def insertion_sort(arr): # tri insertion
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i-1
        while j >=0 and key_item < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key_item
    return arr

def binary_search_iterative(arr, x): # dichotomie itératif
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

def binary_search_recursive(arr, left, right, x): # dichotomie récursif
    if right >= left:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_recursive(arr, left, mid - 1, x)
        else:
            return binary_search_recursive(arr, mid + 1, right, x)
    else:
        return -1




np.random.seed(1234)
t1 = np.random.randint(1, 45, size=5)
print("nombres aléatoires :")
print(t1)

T = int(input("1 pour tri fusion, 2 pour tri cocktail, 3 pour tri insertion :"))
if T == 1:
    np.random.seed(1234)
    t1 = merge_sort_recursive(t1)
    print("tri fusion :")
    print(t1)
if T == 2:
    np.random.seed(1234)
    t1 = np.random.randint(1, 45, size=5)
    print("tri cocktail")
    print(cocktail_sort(t1))
if T ==3:
    np.random.seed(1234)
    t1 = np.random.randint(1, 45, size=5)
    print("tri par insertion")
    t1 = insertion_sort(t1)
    print(t1)

np.random.seed(1234)
t1 = np.random.randint(1, 45, size=5)
t1.sort()

x = int(input("Entrez le nombre à rechercher (algorithme de recherche dichotomique itératif) :"))
result = binary_search_iterative(t1, x)
if result != -1:
    print("Le nombre", x, "a été trouvé à l'index", result)
else:
    print("Le nombre", x, "n'a pas été trouvé dans le tableau")

t1 = np.sort(t1)
x = int(input("Entrez le nombre à rechercher (algorithme de recherche dichotomique récursif) :"))
result = binary_search_recursive(t1, 0, len(t1) - 1, x)
if result != -1:
    print("Le nombre", x, "a été trouvé à l'index", result)
else:
    print("Le nombre", x, "n'a pas été trouvé dans le tableau")

H = int(input("voulez vous afficher un  histogramme?(1 oui 2 non):"))
if H == 1:
    s = int(input("combien de fois voulez vous répeter l'experience ? :"))
    np.random.seed(1234)
    t1 = np.random.randint(1, 45, size=s)
    plt.hist(t1, bins=range(1, 46), align='left', rwidth=1)
    plt.xlabel('Numéros tirés')
    plt.ylabel('Nombre de fois')
    plt.title('Histogramme loto')
    plt.show()
if H == 2:
    print('ok ok')