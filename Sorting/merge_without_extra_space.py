'''
	Function to merge two sorted arrays in one
	without using extra space.

	Function Arguments: array a with size n and array b with size m.
	Return Type: none

	Contributed By: Nagendra Jha
'''


def nextGap(gap):
    if (gap <= 1):
        return 0
    return ((gap + 1) // 2)


def merge(a, n, b, m):
    gap = n + m
    gap = nextGap(gap)
    while (gap > 0):
        i = 0

        # comparing elements in the first array.
        while (i + gap < n):
            if (a[i] > a[i + gap]):
                a[i], a[i + gap] = a[i + gap], a[i]
            i += 1

        j = max(0, gap - n)

        # comparing elements in both the arrays
        while (i < n and j < m):
            if (a[i] > b[j]):
                a[i], b[j] = b[j], a[i]
            i += 1
            j += 1

        # comparing elements in second array
        if (j < m):
            j = 0
            while (j + gap < m):
                if (b[j] > b[j + gap]):
                    b[j], b[j + gap] = b[j + gap], b[j]
                j += 1
        gap = nextGap(gap)