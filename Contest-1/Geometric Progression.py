def termOfGP(A,B,N):
    r=B/A #Common ration of GP
    return A*pow(r,N-1) #Nth term is a(r^N-1)
for _ in range(int(input())):
    a,b=map(int,input().split())
    n=int(input())
    print(int(termOfGP(a,b,n)))