
def bubble_sort_with_error(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # Pokud nebyly žádné dva prvky vyměněny vnitřní smyčkou, přeruš cyklus
        if not swapped:
            break

    return arr

# Testovací pole s funkcí
test_array = [64, 25, 12, 22, 11]
sorted_array = bubble_sort_with_error(test_array)