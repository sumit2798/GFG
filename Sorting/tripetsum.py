def find3Numbers(a, n, sum):
    # sort the array
    a.sort()

    for i in range(n - 2):
        l = i + 1
        r = n - 1

        # find the pair which after adding with arr[i]
        # sum to sum
        while (l < r):
            curr_sum = a[i] + a[l] + a[r]
            if (curr_sum == sum):
                return 1
            elif (curr_sum < sum):
                l += 1
            else:
                r -= 1
    return 0