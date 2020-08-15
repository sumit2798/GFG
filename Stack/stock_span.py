#Python 3
'''
Function Arguments :
		@param  : price( array containing price on days) , n size of list input.
		@return : List containg corresponding span values
'''
def calculateSpan(a,n):
    S = [0 for i in range(n+1)] # list consisting of span values.

    # Create a stack and push index of fist element to it
    st = []
    st.append(0)

    # Span value of first element is always 1
    S[0] = 1

    # Calculate span values for rest of the elements
    for i in range(1, n):

        # Pop elements from stack whlie stack is not
        # empty and top of stack is smaller than price[i]
        while (len(st) > 0 and a[st[-1]] <= a[i]):
            st.pop()

            # If stack becomes empty, then price[i] is greater
        # than all elements on left of it, i.e. price[0],
        # price[1], ..price[i-1]. Else the price[i] is
        # greater than elements after top of stack
        S[i] = i + 1 if len(st) <= 0 else (i - st[-1])

        # Push this element to stack
        st.append(i)

    return S[0:n] # return first n-1 entries from the span list, as last entry is dummy.
