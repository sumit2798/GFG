def sortAbs(a, n, k):
    a= sorted(a,key = lambda x :(abs(x-k)) ) # using lambda expression
    return a