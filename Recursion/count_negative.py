def count_negative(arr):
    count = 0
    i = 0 
    j = len(arr[0]) - 1
    while j >= 0 and i < len(arr):
        if arr[i][j] < 0:
            count += j+1
            i += 1
        else:
            j -= 1
    return count
arr = [[-3,-2,-1,1],[-2,2,3,4],[4,5,7,8]]
print(count_negative(arr))