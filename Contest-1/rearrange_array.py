#Rearrange an array with O(1) extra space
def arrange(arr, n):
    # changing the array elements
    # to rearrange
    for i in range(0, n):
        arr[i] += (arr[arr[i]] % n) * n

    # reverting the elements
    for i in range(0, n):
        arr[i] = arr[i]
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print(arrange(arr,n))
    """
    3
2
1 0
5
4 0 2 1 3
4
3 2 0 1

Output:
0 1
3 4 2 0 1
1 0 3 2
    
    """