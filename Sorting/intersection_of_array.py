def printIntersection(arr1, arr2, n, m):
    i = 0
    j = 0
    flag = False
    l = []
    while (i < n and j < m):
        if i > 0 and arr1[i - 1] == arr1[i]:
            i += 1
            continue
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            # print(arr2[j],end=" ")
            l.append(arr2[j])
            flag = True
            i += 1
            j += 1

    if flag is False:
        l.append(arr2[j])
    return l