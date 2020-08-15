def xorPair(arr, n, x):
    result = 0
    s = set()
    for i in range(0, n):
        if (x ^ arr[i] in s):
            return True

        s.add(arr[i])
    return False


for _ in range(int(input())):
    m, n = map(int, input().split())
    l = list(map(int, input().split()))
    if (xorPair(l, m, n)):
        print("Yes")
    else:
        print("No")
        """
        2
7 7
2 1 10 3 4 9 5 
5 1
9 9 10 10 3 

Output:
Yes
No

Explanation :
In first case, pair (2,5) give 7. 
Hence answer is "Yes".
 In second case no pair exist such that satisfies the condition hance the answer is "No".
        """