"""
Given an array arr[] of N positive integers.
The task is to find a subsequence with maximum sum such that there should be no adjacent elements
 from the array in the subsequence

"""
def findMaxSum(n):

    incl_prev = arr[0]
    excl_prev = 0
    incl_curr = 0
    excl_curr = 0
    for i in range(1,n):
        excl_curr = max(incl_prev, excl_prev);
        incl_curr = excl_prev + arr[i];

        incl_prev = incl_curr;
        excl_prev = excl_curr;

    return max(incl_curr, excl_curr);


for _ in range(int(input())):
    n = int(input())
    arr=list(map(int,input().split()))

    if (n == 1) :
        print(arr[0])
    else:
        print(findMaxSum(n))

