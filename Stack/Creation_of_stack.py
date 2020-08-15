#Python 3
'''
Function Arguments :
		@param  : a (auxilary array),
		top1 and top2 are declared as two tops of stack.
		# initialized value of  tops of the two stacks
        top1 = -1
        top2 = 101
		@return : Accordingly.
'''

# pop element from 1st stack
def pop1(a):
    global top1
    if top1 == -1:
        return -1
    else:
        val = a[top1]
        top1-=1
        return val

# pop element from 2nd stack
def pop2(a):
    global top2
    if top2 == 101:  # size of array is 101, so if stack is empty.
        return -1
    else:
        val = a[top2]
        top2+=1
        return val

# push element to second stack
def push2(a,x):
    global top1
    global top2
    if top1 < top2-1:
        top2-=1
        a[top2] = x

# push element to first stack
def push1(a,x):
    global top1
    global top2
    if top1 < top2-1:
        top1+=1
        a[top1] = x