def binarySearch(arr, l, r, x):
    if (r >= l):

        # finding mid
        mid = l + (r - l) // 2

        # if mid element is equal to x
        if (arr[mid] == x):
            return mid

        # if element at mid-1 is equal to x
        if (mid > l and arr[mid - 1] == x):
            return mid - 1

        # element at mid+1 is equal to x
        if (mid < r and arr[mid + 1] == x):
            return mid + 1

        # if element at mid is greater than x
        # recruse for left half
        if (arr[mid] > x):
            return binarySearch(arr, l, mid - 2, x)

        # if element at mid is less than x
        # recurse for right half
        return binarySearch(arr, mid + 2, r, x)

    # if element is not found
    return -1;


def closer(arr, n, x):
    return binarySearch(arr, 0, n - 1, x)