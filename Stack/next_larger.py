
# Stack Functions to be used for our stack
def createStack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def push(stack, x):
    stack.append(x)


def pop(stack):
    if isEmpty(stack):
        print("Error : stack underflow")
    else:
        return stack.pop()

'''
Function Arguments : 
		@param  : arr(given array), n(size of array)
		@return : An array of length n denoting the next greater elements 
		          for all the array elements
'''
def nextLargerElement(arr,n):

    next_greater = [-1 for i in range(n)] # our answer list, initialized to -1.
    s = createStack()
    element = 0
    next = 0

    # push the first element to stack
    push(s, [arr[0],0])

    # iterate for rest of the elements
    for i in range(1, n, 1):
        next = arr[i]

        if isEmpty(s) == False:

            # if stack is not empty, then pop an element from stack
            elem = pop(s) # value, index pair popped from stack
            element = elem[0] # get the value stored in the pair
            curr_index = elem[1] # get the value stored in the pair

            '''If the popped element is smaller than next, then 
                a) print the pair 
                b) keep popping while elements are smaller and 
                   stack is not empty '''
            while element < next:
                next_greater[curr_index] = next # assign value of nge to corresponding index
                if isEmpty(s) == True:
                    break
                elem = pop(s)
                element = elem[0]
                curr_index = elem[1]

            '''If element is greater than next, then push 
               the element back '''
            if element > next:
                push(s, [element,curr_index])

        '''push next to stack so that we can find 
           next greater for it '''
        push(s, [next,i])

    '''After iterating over the loop, the remaining 
       elements in stack do not have the next greater 
       element, so let -1 be for them, as initialized. '''

    return next_greater
