#Fibonnaci Iterative solution

def fibonnaci_iterative(num):
    a = 0
    b = 1
    result = []
    for i in range(num):
        a,b = b , a+b
        result.append(a)
    return a

fibonnaci_iterative(10)


#Fibonnaci Recursive solution

def fibonnaci_recursive(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibonnaci_recursive(num-1) + fibonnaci_recursive(num-2)  

fibonnaci_recursive(10)


#Fibonnaci Recursive solution with Memoization

def fibonnaci_memo(num):
    cache = [None] * (num + 1)
    return fib_cache(num, cache)
    
def fib_cache(num, cache):
    if num == 0 or num == 1:
        return num
    if cache[num] != None:
        return cache[num]
    else:
        cache[num] = (fib_cache(num-1,cache) + fib_cache(num-2,cache))
    return cache[num]

fibonnaci_memo(10)
