def binary_search_recursive(arr, left, right, x):
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


t1 = np.sort(t1)
x = int(input("Entrez un numéro de recherche: "))
result = binary_search_recursive(t1, 0, len(t1) - 1, x)

if result != -1:
    print("Le numéro est présent à l'index", result)
else:
    print("Le numéro n'est pas présent dans le tableau.")
