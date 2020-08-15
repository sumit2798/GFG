def maxWater(height, n):
    # To store the maximum water so far
    maximum = 0;

    # Both the pointers are pointing at the first
    # and the last buildings respectively
    i = 0
    j = n - 1

    # While the water can be stored between
    # the currently chosen buildings
    while (i < j):

        # Update maximum water so far and increment i
        if (height[i] < height[j]):
            maximum = max(maximum, (j - i - 1) * height[i]);
            i += 1;

        # Update maximum water so far and decrement j
        elif (height[j] < height[i]):
            maximum = max(maximum, (j - i - 1) * height[j]);
            j -= 1;

        # Any of the pointers can be updated (or both)
        else:
            maximum = max(maximum, (j - i - 1) * height[i]);
            i += 1;
            j -= 1;

    return maximum;
"""
Given an integer array representing the heights of N buildings, 
the task is to delete N-2 buildings such that the water that can be trapped
 between the remaining two building is maximum.
Note: The total water trapped between two buildings
 is gap between them (number of buildings removed) multiplied by height of the smaller building.
Input:
2
6
2 1 3 4 6 5
2
2 1
Output:
8
0

Explanation:
Testcase1: The heights are 2 1 3 4 6 5. So we choose the following buildings 2 1 3 4 6 5  and remove others. So total removed buildings is equal to 4, 
now the height of smaller one is 2.
 So answer is 2 * removed buildings = 2*4 = 8. 
 There is no answer greater than this.
Testcase2: The heights are 2 1. So we choose the following buildings 2 5  and remove others.
 But there is no other buildings to be removed so total removed = 0. 
  Now the height of smaller one is 2.
   So answer is 2 * removed buildings = 2*0 = 0.
"""