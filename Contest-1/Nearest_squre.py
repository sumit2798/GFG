import math
#You are given a number N. You need to find the perfect square that is nearest to it.
# If two perfect squares are at the same distance to N, then print the greater perfect square
def ps(n):
    num=int(math.sqrt(n))
    return num*num==n

testcases=int(input())
while(testcases>0):
    n=int(input())
    smaller=0
    greater=0
    if(ps(n) is True):
        smaller=int(math.sqrt(n))-1
        greater=int(math.sqrt(n))+1
    else:
        smaller=math.floor(math.sqrt(n))
        greater=math.ceil(math.sqrt(n))
    if(abs(smaller*smaller-n)<abs(greater*greater-n)):
        print(int(smaller*smaller))
    else:
        print(int(greater*greater))
    testcases-=1
"""
3
1
56
100
Output:
0
49
81

Explanation:
Testcase1: 0 and 4 are near to 1. 0 is nearest.
Testcase2: 49 and 64 are near to 56. 49 is nearest.
Testcase3: 81 and 121 are near to 100. 81 is nearest.
"""