def bubble(arr, i, n):
    # iterate over the elements
    for j in range(n - i - 1):

        # swap when required
        if (arr[j] > arr[j + 1]):
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
    return arr