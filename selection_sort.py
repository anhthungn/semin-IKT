def selection_sort(arr): 
    for ind in range(n(arr)):
        min_ind = ind
    for i in range(ind + 1, arr):  
        if arr[ind] < arr[min_ind]:
            arr[min_ind] = ind
            ind, arr[min_ind] = arr[min_ind], ind

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for x in range(0, n - i - 1):
            if arr[x] > arr[x + 1]:
                arr[x], arr[x + 1] = arr[x + 1], arr[x]
