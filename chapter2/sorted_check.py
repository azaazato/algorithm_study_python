arr = [1,2,3,4,5,6]

def is_array_sorted(arr, n):
    if n == 1:
        return 1
    return 0 if arr[n-2] > arr[n-1] else is_array_sorted(arr, n-1)

print(is_array_sorted(arr, len(arr)))
