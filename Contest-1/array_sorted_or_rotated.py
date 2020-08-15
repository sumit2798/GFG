def II(arr, n):
    i = 0
    while (i < n - 1 and arr[i] <= arr[i + 1]):
        i += 1

    if i == n - 1:
        return False

    i += 1

    while (i < n - 1 and arr[i] <= arr[i + 1]):
        i += 1

    if (i == n - 1 and arr[n - 1] <= arr[0]):
        return True
    else:
        return False


def DD(arr, n):
    i = 0
    while (i < n - 1 and arr[i] >= arr[i + 1]):
        i += 1

    if i == n - 1:
        return False

    i += 1

    while (i < n - 1 and arr[i] >= arr[i + 1]):
        i += 1

    if (i == n - 1 and arr[n - 1] >= arr[0]):
        return True
    else:
        return False


def checkRotatedAndSorted(arr, n):
    if II(arr, n) == True:
        return True

    if DD(arr, n) == True:
        return True

    return False
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print(maxSubArraySum(arr,n))
"""
Input:
5
4
3 4 1 2
3
1 2 3
4
10 20 30 14
5
30 20 10 50 35
5
30 20 10 50 25

Output:
Yes
No
No
Yes
No

Explanation:
Testcase 1: The array is sorted (1, 2, 3, 4) and rotated twice (3, 4, 1, 2).
Testcase 2: The array is sorted (1, 2, 3) is not rotated.
Testcase 3: The array is sorted (10, 20, 30, 14) is not sorted and rotated as 14 is greater than 10.
"""
