for _ in range(int(input())):
    m,n=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    x=sum(l[:n])
    print(x)
    """
    Input :
1
6 4
1 3 4 1 3 8

Output :
8

Explaination :
Testcase1: Sum of first 4 smallest numbers is 1+1+3+3 = 8
    """