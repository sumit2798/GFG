def minOperations(n):
    if n<=3:
        return n-1
    elif(n%2!=0):
        return (1+min(minOperations(n-1), minOperations(n+1)))
    else:
        return (1+minOperations(n//2))


if __name__=="__main__":
    t = int(input())
    while(t>0):
        n = int(input())
        print(minOperations(n))
        t=t-1
"""
You are given a number N. You need to convert it to 1 in minimum number of operations.

The operations allowed are as follows:

If N is even then divide the number by 2.
If N is odd then you can either add 1 to it or subtract 1 from it.
Using the above operations, find the minimum number of operations require to convert N to 1.
"""