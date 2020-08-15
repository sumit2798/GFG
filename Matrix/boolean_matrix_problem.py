"""
You are given a matrix Mat of m rows and n columns. The matrix is boolean so the elements of the matrix can only be either 0 or 1.
Now, if any row of the matrix contains a 1, then you need to fill that whole row with 1. After doing the mentioned operation, you need to print the modified matrix.
"""
if __name__ == "__main__":
    t = int(input())
    while(t>0):
        matsize = [int(x) for x in input().strip().split()]
        n = matsize[0]
        m = matsize[1]
        mat = [[0 for i in range(m)] for j in range(n)]
        row = [0 for i in range(n)]
        for i in range(n):
            list = [int(x) for x in input().strip().split()]
            for j in range(m):
                mat[i][j] = list[j]
                if(mat[i][j]==1):
                    row[i]=1
        for i in range(n):
            for j in range(m):
                if(row[i]==1):
                    print(1, end=" ")
                else:
                    print(0, end=" ")
            print()
        t=t-1