def factorial(N):
    ans=1
    i=2
    while(i<=N):
        ans*=i #multiplying all the numbers from 2 to N.
        i+=1
    return ans
for _ in range(int(input())):
    n=int(input())
    m=factorial(n)
    print(m)
