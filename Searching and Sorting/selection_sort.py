def selection_sort(arr):
    min_index = 0
    for i in range(0, len(arr)):
        min_index = min_index_finder(arr, i)
        arr = swap(arr, i , min_index)
    return arr

def min_index_finder(arr, i):
    min_index = i
    for index in range(i+1, len(arr)):
        if arr[index] < arr[min_index]:
            min_index = index
    return min_index

def swap(arr, i, min_index):
    if i == min_index:
        return arr
    else:
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
selection_sort([65, 46, 14, 52, 38, 2, 96, 39, 14, 33, 13, 4, 24, 99, 89, 77, 73, 87, 36, 81])