def findMedian(arr, n, brr, m):
    min_i, max_i = 0, n
    i, j, median = 0, 0, 0
    while(min_i<=max_i):
        i = (min_i+max_i)//2
        j = ((n+m+1)//2)-i

        if(i<n and j>0 and brr[j-1]>=arr[i]):
            min_i = i+1
        elif(i>0 and j<m and brr[j]<arr[i-1]):
            max_i = i-1
        else:
            if i==0:
                median = brr[j-1]
            elif j==0:
                median = arr[i-1]
            else:
                median = max(arr[i-1], brr[j-1])
            break
    if((n+m)%2==1):
        return median
    if(i==n):
        res = (median+brr[j])//2
    if(j==m):
        res = (median + min(arr[i], brr[j]))//2
    res = (median + min(arr[i], brr[j]))//2

    return res

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        n_m = [int(x) for x in input().strip().split()]
        n, m= n_m[0], n_m[1]
        arr = [int(x) for x in input().strip().split()]
        brr = [int(x) for x in input().strip().split()]
        if(n<m):
            print(findMedian(arr, n, brr, m))
        else:
            print(findMedian(brr, m, arr, n))
        t=t-1