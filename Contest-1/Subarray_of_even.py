def maxEvenOdd(arr, n):
    msf = 1
    cmax = 1

    for i in range(1, n):
        if ((arr[i - 1] % 2 == 0 and arr[i] % 2 != 0) or (arr[i - 1] % 2 != 0 and arr[i] % 2 == 0)):

            cmax += 1
            msf = max(msf, cmax)
        else:
            cmax = 1

    return msf
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print(maxEvenOdd(arr,n))
"""
Input:
3
5
10 12 14 7 8
2
4 6
3
1 2 3

Output:
3
1
3

Example:
Testcase 1: The max length of subarray is 3 and the subarray is {14 7 8}. 
Here the array starts as an even element and has odd and even elements alternately.
Testcase 2: The array contains {4 6}.
 So, we can only choose 1 element as that will be the max length subarray.
Testcase 3: The subarray with max length 3 is {1 2 3}.
 It starts with an odd element and has even and odd elements alternately.
"""