#User function Template for python3

# arr[] : the input array
# N : size of the input array

# return the number of subarrays with equal 0s and 1s
def countSubarrWithEqualZeroAndOne(arr, N):
    l = []
    for i in arr:
        if i==0:
            l.append(-1)
        else:
            l.append(1)
    count = 0
    add = 0
    h = {}
    for i in l:
        add+=i
        if add == 0:
            count+=1
        if add in h.keys():
            count+=h[add]
            h[add]+=1
        else:
            h[add] = 1
    return count




#{
#  Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):

        n=int(input())
        arr=[int(x) for x in input().strip().split()]


        print(countSubarrWithEqualZeroAndOne(arr, n))

        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends