def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        first_half = arr[:len(arr)//2]
        second_half = arr[len(arr)//2:]
        merge_sort(first_half)
        merge_sort(second_half)
        sorter(arr, first_half, second_half)

def sorter(arr, first_half, second_half):
    i=0
    j=0
    k=0
    while i < len(first_half) and j < len(second_half):
        if first_half[i] < second_half[j]:
            arr[k] = first_half[i]
            i +=1
        else:
            arr[k] = second_half[j]
            j += 1
        k +=1
    while i < len(first_half):
        arr[k] = first_half[i]
        i += 1
        k += 1
    while j < len(second_half):
        arr[k] = second_half[j]
        j += 1
        k += 1

arr = [45,67,23,45,21,24,7,2,6,4,90]
merge_sort(arr)
print(arr)