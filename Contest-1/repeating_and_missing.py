if __name__ == "__main__":
    t = int(input())
    while(t>0):
        n = int(input())
        list = [int(x) for x in input().strip().split()]
        for i in range(0, n):
            if list[abs(list[i])-1]>0:
                list[abs(list[i])-1] = -list[abs(list[i])-1]
            else:
                print(abs(list[i]), end=" ")

        for i in range(n):
            if list[i]>0:
                print(i+1)
        t=t-1
"""
Given an unsorted array A[] of size N of positive integers. 
One number 'a' from set {1, 2, …N} is missing and one number 'b' occurs twice in array. 
The task is to find the repeating and the missing.
"""