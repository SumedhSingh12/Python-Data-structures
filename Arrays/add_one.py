def add(arr):
    carry = 1
    if len(arr)==0:
        return [1]
    else:
        for i in range(len(arr)-1, -1, -1):
            arr[i] = (arr[i] + carry) % 10
            if arr[i] == 0:
                carry = 1
            else:
                carry = 0
                break
    if carry==1:
        return [1] + arr
    else:
        return arr
print(add([1,2,9,9]))