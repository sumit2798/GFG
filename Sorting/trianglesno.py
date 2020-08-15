''' Function should return the total number of triangles
    which can be made by selecting triplets from the given array'''


def findNumberOfTriangles(arr, n):
    arr.sort()
    count = 0

    # traversing through the array elements
    for i in range(n - 2):
        k = i + 2
        for j in range(i + 1, n):
            # Traversing all the elements
            # to check if there is any element exists
            # which can satisfy the condition of triangle
            # with the elements at ith and jth index
            while (k < n and arr[i] + arr[j] > arr[k]):
                k += 1
            count += k - j - 1
    return count