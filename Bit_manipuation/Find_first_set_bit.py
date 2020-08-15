import  math
def getFirstSetBit(n):
    if(n==0):
        return 0
    return math.ceil(math.log2(n&-n)+1
n=int(input())
print(getFirstSetBit(n))
"""
Input:
3
18
12
0

Output:
2
3
0
"""