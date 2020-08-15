# Python3 program to print all elements
# of given matrix in diagonal order
R = 5
C = 4


def isValid(i, j):
    if (i < 0 or i >= R or j >= C or j < 0):
        return False
    return True


def diagonalOrder(arr):
    # through this for loop we choose each element
    # of first column as starting point and print
    # diagonal starting at it.
    # arr[0][0], arr[1][0]....arr[R-1][0]
    # are all starting points
    for k in range(0, R):
        print(arr[k][0], end=" ")

        i = k - 1

        j = 1

        while (isValid(i, j)):
            print(arr[i][j], end=" ")
            i -= 1
            j += 1  # move in upright direction

        print()

    # Through this for loop we choose each
    # element of last row as starting point
    # (except the [0][c-1] it has already been
    # processed in previous for loop) and print
    # diagonal starting at it.
    # arr[R-1][0], arr[R-1][1]....arr[R-1][c-1]
    # are all starting points

    # Note : we start from k = 1 to C-1;
    for k in range(1, C):
        print(arr[R - 1][k], end=" ")

        # set row index for next point in diagonal
        i = R - 2

        # set column index for next point in diagonal
        j = k + 1

        # Print Diagonally upward
        while (isValid(i, j)):
            print(arr[i][j], end=" ")
            i -= 1
            j += 1  # move in upright direction

        print()

    # Driver Code


arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16],
       [17, 18, 19, 20]]
diagonalOrder(arr)
