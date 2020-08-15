#Python 3
'''
Function Arguments :
      @param  : a(given array), n (size of array)
      @return : None, print the required Maxofmin array.
'''

def printMaxOfMin(a,n):
    stack = []  # Used to find previous and next smaller

    #Lists to store previous and next smaller
    left = [-1 for i in range(n)] # initialized with -1
    right = [n for i in range(n)] # initialized with n

    '''
        Fill elements of left[] using logic discussed on 
        https://www.geeksforgeeks.org/next-greater-element/
    '''
    for i in range(n):
        while len(stack) and a[stack[-1]]>=a[i]:
            stack.pop()
        if len(stack):
            left[i] = stack[-1]
        stack.append(i)

    # empty the stack for use in right.
    stack = []

    # fill elements of right using same logic
    for i in range(n-1,-1,-1):
        while len(stack) and a[stack[-1]]>=a[i]:
            stack.pop()
        if len(stack):
            right[i] = stack[-1]
        stack.append(i)

    # create and initialize ans array
    ans= [0 for i in range(n+1)]

    '''Fill answer array by comparing minimums of all 
     lengths computed using left[] and right[] '''
    for i in range(n):
        # length of the interval
        length = right[i]-left[i]-1
        ans[length] = max(ans[length],a[i])

    '''
        Some entries in ans[] may not be filled yet. Fill  
        them by taking values from right side of ans[] .
    '''
    for i in range(n-1,-1,-1):
        ans[i] = max(ans[i],ans[i+1])

    # print ans from len 1 to n
    return ans[1:]
