def most_frequent(arr, k):
    result = {}
    for num in arr:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1
    bucket = [None]*len(arr)
    for num in result:
        if bucket[result[num]] == None:
            bucket[result[num]] = [num]
        else:
            bucket[result[num]].append(num)
    count = k
    result = []
    for i in range(len(bucket)-1, -1, -1):
        if count == 0:
            break
        elif bucket[i] == None:
            continue
        else:
            for j in range(len(bucket[i])):
                if count != 0:
                    count -= 1
                    result.append(bucket[i][j])
                else:
                    break
most_frequent([1,6,2,1,6,1,6], 2)