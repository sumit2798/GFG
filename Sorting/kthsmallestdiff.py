import io
import sys

# Contributed by : Nagendra Jha

def count(a,mid):
    ans=0
    j=0
    for i in range(1,len(a)):
        while(j<i and a[i]-a[j] > mid):
            j+=1
        ans+=i-j

    return ans

def small(a,k):
    a.sort()
    l,r=0,a[len(a)-1]-a[0]

    while(r>l):
        mid = (l+r)//2
        if(count(a,mid)<k):
            l=mid+1
        else:
            r = mid
    return r

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n,k = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        print(small(a,k))
        """
        1
6 2
1 3 4 1 3 8
Output :
0

Explanation :
Testcase1: First smallest difference is 0 , between the pair (1,1) 
and second smallest absolute difference difference is also 0 between the pairs (3,3).
        """