def maxIndexDiff(arr,n):
    '''
     Construct LMin[] such that LMin[i] stores the minimum value
       from (arr[0], arr[1], ... arr[i])
    '''

    LMin=[0 for i in range(n)]
    LMin[0]=arr[0]
    for i in range(1,n):
        LMin[i] = min(arr[i],LMin[i-1])

    '''
    Construct RMax[] such that RMax[j] stores the maximum value 
       from (arr[j], arr[j+1], ..arr[n-1])
    '''
    RMax=[0 for i in range(n)]
    RMax[n-1]=arr[n-1]

    for i in range(n-2,-1,-1):
        RMax[i]=max(arr[i],RMax[i+1])

    '''
    Traverse both arrays from left to right to find optimum j - i 
        This process is similar to merge() of MergeSort
    '''
    i,j,maxDiff=0,0,-1
    while j<n and i<n:
        if LMin[i]<=RMax[j]:
            maxDiff=max(maxDiff,j-i)
            j=j+1
        else:
            i=i+1
    return maxDiff
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print(maxIndexDiff(arr,n))
    """
    2
2
1 10
9
34 8 10 3 2 80 30 33 1

Output:
1
6

Explanation:
Testcase 1: A[0]<=A[1] so (j-i) is 1-0 = 1.
Testcase 2:  In the given array A[1] < A[7] satisfying the required condition(A[i] <= A[j]) 
thus giving the maximum difference of j - i which is 6(7-1).
    """
