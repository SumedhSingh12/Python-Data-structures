def fact(num):
    cache = [None] * (num+1)
    return factorial(num,cache)
def factorial(num,cache):
    if num == 0 or num == 1:
        return 1
    if cache[num] != None:
        return cache[num]
    else:
        cache[num] = num * factorial(num-1,cache)
    return cache[num] 

print(len(str(fact(100))))
