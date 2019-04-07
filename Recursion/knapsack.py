def knapsack(n, c, weight, value, cache=None):
    if cache == None:
        cache = [[None]*(n+1)]*(c+1)
    if n==0 or c==0:
        return 0
    elif weight[n] > c:
        cache[c][n] = knapsack(n-1, c, weight, value,cache)
    elif cache[c][n] != None:
        return cache[c][n]
    else:
        cache[c][n] = max(knapsack(n-1, c, weight, value,cache), value[n] + knapsack(n-1, c-weight[n], weight, value, cache))   
    return cache[c][n]

weight = [None,1,2,4,2,5]
value = [None, 5,3,5,3,2]
knapsack(5,10,weight, value)
    