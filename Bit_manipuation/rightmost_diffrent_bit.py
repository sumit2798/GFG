def getRightMostSetBit(n):
    return math.log2(n & -n) + 1


def posOfRightMostDiffBit(m, n):
    if m == n:
        return -1
    return getRightMostSetBit(m ^ n)
m,n=map(int,input().split())
print(getRightMostSetBit(m,n))
"""
2
11 9
52 4

Output:
2
5

Explanation:
Tescase 1: Binary representaion of the given numbers are: 1011 and 1001, 2nd bit from right is different.
Testcase 2: Binary representation of the given numbers are:  ‭110100‬ and 0100, 5th bit fron right is different.
"""