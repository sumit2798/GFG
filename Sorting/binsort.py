def binSort(arr, n):
    type0 = 0
    type1 = n - 1

    # using segregation method
    while (type0 < type1):
        if (arr[type0] == 1):
            (arr[type0],
             arr[type1]) = (arr[type1],
                            arr[type0])
            type1 -= 1
        else:
            type0 += 1