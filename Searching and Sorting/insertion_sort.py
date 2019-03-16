def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while(j >=0 and arr[j] > key):
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr
insertion_sort([65, 46, 14, 52, 38, 2, 96, 39, 14, 33, 13, 4, 24, 99, 89, 77, 73, 87, 36])