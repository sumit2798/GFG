'''Function takes sorted arrays as argument and returns
    a single array which contains all the elements of those 3
    arrays in non decreasing order'''

# Back-end complete function Template for Python 3

'''Function takes sorted arrays as argument and returns
    a single array which contains all the elements of those 3
    arrays in non decreasing order'''


def mergeThree(A, B, C):
    # Get Sizes of three arrays
    n = len(A)
    m = len(B)
    p = len(C)

    merged_array = []  # array for storing result

    i = 0
    j = 0
    k = 0

    # minimum valued array gets exhausted here
    while (i < n and j < m and k < p):
        merged_array.append(min(A[i], B[j], C[k]))

        if (merged_array[-1] == A[i]):
            i += 1
        elif (merged_array[-1] == B[j]):
            j += 1
        else:
            k += 1

    # second minimum valued array gets exhausted here
    while (i < n and j < m):
        merged_array.append(min(A[i], B[j]))

        if (merged_array[-1] == A[i]):
            i += 1
        elif (merged_array[-1] == B[j]):
            j += 1
    while (i < n and k < p):
        merged_array.append(min(A[i], C[k]))

        if (merged_array[-1] == A[i]):
            i += 1
        elif (merged_array[-1] == C[k]):
            k += 1
    while (j < m and k < p):
        merged_array.append(min(B[j], C[k]))

        if (merged_array[-1] == B[j]):
            j += 1
        elif (merged_array[-1] == C[k]):
            k += 1
    while (i < n):
        merged_array.append(A[i])
        i += 1
    while (j < m):
        merged_array.append(B[j])
        j += 1
    while (k < p):
        merged_array.append(C[k])
        k += 1

    return merged_array