#Python 3
def push(x):
    '''
    :param x: value to be inserted
    :return: None

    queue_1 = [] # first queue
    queue_2 = [] # second queue
    '''
    global queue_1
    global queue_2

    queue_2.append(x) # append value in the queue

    while len(queue_1):
        queue_2.append(queue_1[0]) # insert at back of queue
        queue_1.pop(0) # remove top of queue

    # transfers all elements from queue 2 to queue 1, by swapping the names
    queue_1 , queue_2 =queue_2 , queue_1

def pop():
    '''
    :return: the value of top of stack and pop from it.
    '''
    global queue_1
    global queue_2
    if len(queue_1):
        return queue_1.pop(0)
    else:
        return -1