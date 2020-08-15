def countOccurence(arr, n, k):
    count = 0
    # k must be greater than 1 to get some output
    if k < 2:
        return 0

    '''
    Step 1: Create a temporary array (contains element 
	and count) of size k-1. Initialize count of all 
	elements as 0, count is second value of pair.
	'''
    temp = [[0, 0] for i in range(k - 1)]

    # Step 2: Process all elements of input array
    for i in range(n):
        '''
        If arr[i] is already present in 
        the element count array, then increment its count
        '''
        j = 0
        while j < k - 1:
            if temp[j][0] == arr[i]:
                temp[j][1] += 1
                break
            j += 1

        # If arr[i] is not present in temp[]
        if j == k - 1:
            l = 0
            while l < k - 1:
                if temp[l][1] == 0:
                    temp[l][0] = arr[i]
                    temp[l][1] = 1
                    break
                l += 1

            ''' If all the position in the temp[] are filled, then 
                 decrease count of every element by 1'''
            if l == k - 1:
                for l in range(k - 1):
                    temp[l][1] -= 1
    # Step 3: Check actual counts of potential candidates in temp[]
    for i in range(k - 1):
        ac = 0  # actual count of elements
        for j in range(n):
            if arr[j] == temp[i][0]:
                ac += 1
        # If actual count is more than n/k, then count it
        if ac > (n // k):
            count += 1
    return count
