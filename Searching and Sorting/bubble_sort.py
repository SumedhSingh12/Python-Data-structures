def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for k in range(i):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
    return arr

bubble_sort([65, 46, 14, 52, 38, 2, 96, 39, 14, 33, 13, 4, 24, 99, 89, 77, 73, 87, 36, 99])