"""

Given an array A[] and a range [a, b]. The task is to partition the array around the range such that array is divided in three parts.
1) All elements smaller than a come first.
2) All elements in range a to b come next.
3) All elements greater than b appear in the end.
The individual elements of three sets can appear in any order. You are required to return the modified arranged array.


"""


def threeWayPartition(arr, n, lowVal, highVal):
    # Code here
    s = i = 0
    e = n - 1
    while (i <= e):

        # swapping the element with those at start
        # if array element is less than lowVal
        if arr[i] < lowVal:
            arr[i], arr[s] = arr[s], arr[i]
            i += 1
            s += 1
        # swapping the element with those at end
        # if array element is greater than highVal
        elif arr[i] > highVal:
            arr[i], arr[e] = arr[e], arr[i]
            e -= 1

        # else move ahead
        else:
            i += 1
    return arr