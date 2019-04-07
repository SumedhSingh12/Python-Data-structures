def lcs(p,q):
    if len(p) == 0 or len(q) == 0:
        return 0
    elif p[-1] == q[-1]:
        return 1+lcs(p[:len(p)-1], q[:len(q)-1])
    else:
        return max(lcs(p[:len(p)-1], q), lcs(p, q[:len(q)-1]))
print(lcs("ABDB","ABKJ"))

def lcs_memo(p,q, n=0,m=0 ,cache=None):
    if cache==None:
        n = len(p)
        m=len(q)
        cache = [[None]*(m+1) for i in range(n+1)] 
    if n == 0 or m == 0:
        return 0
    elif p[-1] == q[-1]:
        cache[n][m] =  1+lcs_memo(p[:-1], q[:-1], n-1,m-1, cache)
        return cache[n][m]
    elif cache[n][m]:
        return cache[n][m]
    else:
        cache[n][m] =  max(lcs_memo(p[:-1], q,n-1, m, cache), lcs_memo(p, q[:-1], n, m-1,cache))
        return cache[n][m]
print(lcs("ABCDGH","AEDFHR"))