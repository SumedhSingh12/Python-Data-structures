def quick_sort(arr,fromIndex=0, toIndex=len(arr)-1):
    if fromIndex >= toIndex:
        return arr
    else:
        partition = partitioner(arr, fromIndex, toIndex)
        quick_sort(arr, fromIndex, partition)
        quick_sort(arr, partition+1, toIndex)
    return arr
def partitioner(arr, fromIndex, toIndex):
    pivot = arr[fromIndex]
    i = fromIndex -1
    j = toIndex + 1
    while i < j:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i] , arr[j] = arr[j] , arr[i]
    return j
quick_sort([45,67,23,45,21,24,7,2,6,4,90])