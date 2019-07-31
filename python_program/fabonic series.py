# use of fabonic series
def fab(n):
    res = []
    a, b = 0,1
    while a<n:
        res.append(a)
        a,b = b, a+b
        return res

fa = fab(100)
