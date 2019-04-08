'''Staircase problem with only two possibilities of steps: 1 & 2'''
def staircase(n):
    if n==0 or n==1:
        return 1
    else:
        return staircase(n-1) + staircase(n-1)
def staircase_memo(n, cache=None):
    if cache == None:
        cache = [1,1]+([None] * (n))
    if cache[n]:
        return cache[n]
    else:
        cache[n] = staircase_memo(n-1, cache) + staircase_memo(n-2, cache)
        return cache[n]
def staircase_bottomup(n):
    cache = [1,1]
    for i in range(2,n+1):
        cache.append(cache[i-1] + cache[i-2])
    return cache[n]

'''Staircase problem with the possibilities of steps passed as an argument'''
def staircase_steps(n, steps, total = 0):
    if n==0 or n==1:
        return 1
    for i in steps:
        if i < n:
            total += staircase_steps(n-i, steps, total)
    return total
def staircase_steps_bottom_up(n, steps):
    cache = [1,1]
    total = 0
    for i in range(2, n+1):
        for j in steps:
            if j < i:
                total += cache[i-j]
        cache.append(total)
    return cache[n]
    
#staircase(4)
#staircase_memo(4)
#staircase_bottomup(4)
staircase_steps(4, [1,3,5])
#staircase_steps_bottom_up(4, [1,3,5])