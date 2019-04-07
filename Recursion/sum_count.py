def count_sets(arr, value):
    return rec(arr, value, len(arr)-1)
def rec(arr, value, i, mem={}):
    key = str(value) + ":" + str(i)
    if key in mem:
        return mem[key]
    elif value == 0:
        return 1
    elif value < 0:
        return 0
    elif i < 0:
        return 0
    elif value < arr[i]:
        to_return = rec(arr, value, i-1, mem)
    else:
        to_return = rec(arr, value - arr[i], i-1, mem) + rec(arr, value, i-1, mem)
    mem[key] = to_return
    return to_return
count_sets([2,4,6,10], 16)