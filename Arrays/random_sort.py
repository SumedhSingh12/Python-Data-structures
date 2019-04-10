import random
def random_sort(arr):
    for i in range(len(arr)-1, -1, -1):
        random.seed(20119)
        index = random.randint(0,i)
        arr[index], arr[i] = arr[i], arr[index]
    print(arr)
random_sort([8,6,2,3,1,4,5])