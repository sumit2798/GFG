def isPossible(list, n, m, curmin):
    stuReq = 1
    curSum = 0
    for i in range(n):
        if list[i]>curmin:
            return False
        if curSum+list[i]>curmin:
            stuReq += 1
            curSum = list[i]
            if stuReq>m:
                return False
        else:
            curSum += list[i]
    return True

def solve(list, n, m):
    sum=0
    if n<m:
        return -1
    for i in range(n):
        sum += list[i]

    start = 0
    end = sum
    mid, ans = 0, 10**15
    while(start<=end):
        mid = (start+end)//2
        if(isPossible(list, n, m, mid)):
            if(ans>mid):
                ans = mid
            end=mid-1
        else:
            start=mid+1
    return ans



if __name__ == "__main__":
    t = int(input())
    while(t>0):
        n = int(input())
        list = [int(x) for x in input().strip().split()]
        m = int(input())
        print(solve(list, n, m))
        t = t-1
    """
    Input:
2
4
12 34 67 90
2
3
15 17 20
2
Output:
113
32

Explaination:
Testcase 1:Allocation can be done in following ways:
{12} and {34, 67, 90}     Maximum Pages = 191
{12, 34} and {67, 90}     Maximum Pages = 157
{12, 34, 67} and {90}        Maximum Pages = 113

Therefore, the minimum of these cases is 113, which is selected as output.

Testcase 2: Allocation can be done in following ways:
{15} and {17, 20} Maximum pages = 37
{15, 17} and {20} Maximum Pages = 32

So, the output will be 32.
    
    """