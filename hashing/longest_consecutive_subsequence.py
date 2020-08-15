'''
	Function to return the length of longest subsequence
	with consecutive elements present( order does not matter).

	Function Arguments: array a with size n.
	Return Type: Integer


'''


def findLongestConseqSubseq(arr, n):
    s = set()
    ans = 0

    # Hash all the array elements
    for ele in arr:
        s.add(ele)

        # check each possible sequence from the start
    # then update optimal length
    for i in range(n):

        # if current element is the starting
        # element of a sequence
        if (arr[i] - 1) not in s:

            # Then check for next elements in the
            # sequence
            j = arr[i]
            while (j in s):
                j += 1

            # update  optimal length if this length
            # is more
            ans = max(ans, j - arr[i])
    return ans