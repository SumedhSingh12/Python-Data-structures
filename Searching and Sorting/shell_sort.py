def shell_sort(arr):
    sublist_count = len(arr) // 2
    while sublist_count > 0:
        for i in range(sublist_count):
            insertion_sorter(arr, i , sublist_count)
        sublist_count //= 2

def insertion_sorter(arr, start, sublist_count):
    for i in range(start+sublist_count, len(arr), sublist_count):
        key = arr[i]
        j = i - sublist_count
        while(j+sublist_count >= sublist_count and arr[j] > key):
            arr[j+sublist_count] = arr[j]
            j -= sublist_count
        arr[j+sublist_count] = key

arr = [45,67,23,45,21,24,7,2,6,4,90]
shell_sort(arr)
print(arr)