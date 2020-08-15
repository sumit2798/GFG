"""
Given an array arr[] of N integers arranged in a circular fashion.
Your task is to find the maximum contiguous subarray sum.
"""


def kadane(arr):
    n = len(arr)

    maxend = arr[0]
    maxi = arr[0]

    for i in range(1, n):
        maxend = max(maxend + arr[i], arr[i])
        maxi = max(maxi, maxend)
    return maxi


# finding the part of the array which is to be excluded
def reverseKadane(arr, num):
    sum = 0
    for i in range(0, num):
        sum += arr[i]
    min_minus = 0
    maxi = sum
    for i in range(0, num):
        min_minus = min(min_minus + arr[i], arr[i])
        if min_minus == sum:
            return -999999
        maxi = max(maxi, sum - min_minus)

    return maxi


def circularSubarraySum(arr, n):
    k = kadane(arr)
    rk = reverseKadane(arr, n)

    return max(k, rk)
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print(circularSubarraySum(arr,n))
"""
Input:
3
7
8 -8 9 -9 10 -11 12
8
10 -3 -4 7 6 5 -4 -1
8
-1 40 -14 7 6 5 -4 -1

Output:
22
23
52

Explanation:
Testcase 1: Starting from the last element of the array, i.e, 12, and moving in a circular fashion,
 we have max subarray as 12, 8, -8, 9, -9, 10, which gives maximum sum as 22.
"""