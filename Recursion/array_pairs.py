''' Works only in the case of sorted arrays'''
def array_pairs(arr, k):
    count = 0
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] + arr[j] < k:
            count += j - i
            i += 1
        else:
            j -= 1
    return count
print(array_pairs([2, 3, 4, 6, 9], 12))
    