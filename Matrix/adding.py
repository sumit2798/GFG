def sumMatrix(n1, m1, n2, m2, arr1, arr2):
    if (n1 != n2 or m1 != m2):
        print(-1, end="")
        return

    ans = [[0 for j in range(m1)] for i in range(n1)]

    for i in range(n1):
        for j in range(m1):
            ans[i][j] = arr1[i][j] + arr2[i][j]
            print(ans[i][j], end=" ")
#User function Template for python3



'''
  Function to find sum of matrices
  n1, m1, n2, m2: rows and columns of matrices respectively
  arr1[][], arr2[][]: two input matrices
'''



def main():
    T=int(input())
    while(T>0):
        n1,m1=map(int,input().strip().split())
        arr1=[[0 for j in range(m1)] for i in range(n1)]
        line1=[int(x) for x in input().strip().split()]


        k=0
        for i in range(n1):
            for j in range (m1):
                arr1[i][j]=line1[k]
                k+=1

        k=0

        n2,m2=map(int,input().strip().split())
        arr2=[[0 for j in range(m2)] for i in range(n2)]
        line2=[int(x) for x in input().strip().split()]


        k=0
        for i in range(n2):
            for j in range (m2):
                arr2[i][j]=line2[k]
                k+=1

        k=0



        sumMatrix(n1, m1, n2, m2, arr1, arr2)
        print()

        T-=1

if __name__=="__main__":
    main()
"""
Input:
2
2 3
1 2 3 4 5 6
2 3
1 3 3 2 3 3
3 2
1 2 3 4 5 6
3 2
1 3 3 2 3 3
Output:
2 5 6 6 8 9
2 5 6 6 8 9
"""