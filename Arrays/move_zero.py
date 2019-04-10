def move_zero_opt(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            j = no_zero_finder(arr, i)
            if j != None:
                arr[i], arr[j] = arr[j], arr[i]
            if j == len(arr)-1:
                break
def no_zero_finder(arr, i):
    for j in range(i+1, len(arr)):
        if arr[j] != 0:
            return j
    return None


def move_zero(arr):
    i = 0
    j = 0
    while i < len(arr):
        while arr[i] == 0:
            j += 1
            i += 1
        arr[i], arr[i-j] = arr[i-j], arr[i]
        i += 1
        
move_zero_opt([0,1,0,2,0,0,3])
            