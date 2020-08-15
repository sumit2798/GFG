# User function Template for python3


# r is rows
# c is cols
# mat is matrx
# print it in this function after modifying it
def booleanMatrix(r, c, mat):
    def booleanMatrix(r, c, mat):
        R = r
        C = c
        row = [0] * R
        col = [0] * C

        # Initialize all values of row[] as 0
        for i in range(0, R):
            row[i] = 0

        # Initialize all values of col[] as 0
        for i in range(0, C):
            col[i] = 0

        # Store the rows and columns to be marked
        # as 1 in row[] and col[] arrays respectively
        for i in range(0, R):

            for j in range(0, C):
                if (mat[i][j] == 1):
                    row[i] = 1
                    col[j] = 1

        # Modify the input matrix mat[] using the
        # above constructed row[] and col[] arrays
        for i in range(0, R):

            for j in range(0, C):
                if (row[i] == 1 or col[j] == 1):
                    mat[i][j] = 1

        for i in range(r):
            for j in range(c):
                print(mat[i][j], end=" ")
            print()


def main():
    T = int(input())
    while (T > 0):
        r, c = map(int, input().split())

        mat = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            mat.append(line)

        booleanMatrix(r, c, mat)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends