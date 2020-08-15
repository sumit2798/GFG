import random

inf = 1000000000  # 10^9


# partitioning the array along the pivot
def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):

        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[r], arr[i] = arr[i], arr[r]
    return i


# finding the pivot element and partition the array along that
def randomPartition(arr, l, r):
    n = r - l + 1
    pivot = random.randint(0, n - 1)
    arr[l + pivot], arr[r] = arr[r], arr[l + pivot]
    return partition(arr, l, r)


def kthSmallest(arr, l, r, k):
    # If K is smaller than number of elements in array
    if k > 0 and k <= r - l + 1:

        # find a position for random partition
        pos = randomPartition(arr, l, r)

        # if this pos gives k'th smallest element then return
        if pos - l == k - 1:
            return arr[pos]

        # else recurse for the left or right half accordingly
        if pos - l > k - 1:
            return kthSmallest(arr, l, pos - 1, k)
        return kthSmallest(arr, pos + 1, r, k - pos + l - 1)

    return inf


if __name__ == '__main__':
    test_case = int(input())

    for _ in range(test_case):
        number_of_elements = int(input())
        a = [int(x) for x in input().strip().split(' ')]
        k = int(input())

        print(kthSmallest(a, 0, number_of_elements - 1, k))