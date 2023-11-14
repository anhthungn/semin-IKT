def search(arr, x, low, high):
    if high >= low:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == x:
            return True
        elif mid_value > x:
            return search(arr, x, low, mid - 1)
        else:
            return search(arr, x, mid + 1, high)
        # elif mid_value < x:
        #     low = mid + 1  
        # else:
        #     high = mid - 1  
    else:
        return False

def binary_search(arr, x):
    return search(arr, x, 0, len(arr) - 1)