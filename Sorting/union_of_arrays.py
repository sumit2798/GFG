def mergeArrays(a, b, n, m):
    union_li = list()
    i, j = 0, 0
    while i < n and j < m:
        while i + 1 < n and a[i + 1] == a[i]:
            i += 1
        while j + 1 < m and b[j + 1] == b[j]:
            j += 1
        if a[i] < b[j]:
            union_li.append(a[i])
            i += 1
        elif b[j] < a[i]:
            union_li.append(b[j])
            j += 1
        else:
            union_li.append(b[j])
            j += 1
            i += 1

    # Print remaining elements of the larger array
    while i < n:
        while i + 1 < n and a[i + 1] == a[i]:
            i += 1
        union_li.append(a[i])
        i += 1

    while j < m:
        while j + 1 < m and b[j + 1] == b[j]:
            j += 1
        union_li.append(b[j])
        j += 1
    return union_li