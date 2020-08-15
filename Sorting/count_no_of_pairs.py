''' Function to return the total no of values in array b
    such that x^val > val^x, for a given argument x'''

def count(x,b,n,NoOfb):

    """If x is 0, then there cannot be any value in Y such that
     x^Y[i] > Y[i]^x """
    if(not x):
        return x
    '''
    If x is 1, then the number of pais is equal to number of 
    zeroes in Y[]
    '''
    if(x==1):
        return NoOfb[0]

    '''
    Find number of elements in Y[] with values greater than x 
    upper_bound() gets address of first greater element in Y[0..n-1]
    '''
    index=bisect.bisect_right(b,x)
    ans=0
    if(index<n and b[index]>x):
        ans+=n-index
    '''
    If we have reached here, then x must be greater than 1, 
    increase number of pairs for y=0 and y=1 '''
    ans+=(NoOfb[0]+NoOfb[1])

    #Decrease number of pairs for x=2 and (y=4 or y=3)
    if(x==2):
        ans-= NoOfb[3]+NoOfb[4]
    # Increase number of pairs for x=3 and y=2
    if(x==3):
        ans+=NoOfb[2]

    return ans

''' Function to count total no. of pairs in arrays a and b
    such that x^y > y^x , where x is in a and y is in b'''

def countPairs(a,b,m,n):
    # To store counts of 0, 1, 2, 3 and 4 in array Y
    NoOfb=[0,0,0,0,0]
    for i in range(n):
        if(b[i]<5):
            NoOfb[b[i]]+=1

    # Sort Y[] so that we can do binary search in it
    b.sort()

    total_pairs=0

    # Take every element of X and count pairs with it
    for i in range(m):
        total_pairs+=count(a[i],b,n,NoOfb)
    return total_pairs