# User function Template for python3
'''
Function Arguments :
		@param  : head (given head of linked list), k(value of k)
		@return : None, Just swap the nodes

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''


def getSize(head):
    count = 0
    curr_node = head
    while curr_node:
        count += 1
        curr_node = curr_node.next
    return count


# swap kth node from both ends.
def swapkthnode(head, num, k):
    size = getSize(head)
    if k > size:
        return head

    # if the nodes are in between the linked list.
    if k > 1 and k < size:
        prev_beg = getNthfromBeg(head, k - 1)
        kth_beg = prev_beg.next
        next_beg = kth_beg.next

        prev_end = getNthfromEnd(head, k + 1)
        kth_end = prev_end.next

        next_end = kth_end.next

        # handle case where nodes are adjacent
        if size % 2 == 0 and k == size // 2:
            prev_beg.next = kth_end
            kth_end.next = kth_beg
            kth_beg.next = next_end

            return head

        prev_beg.next = kth_end
        prev_end.next = kth_beg

        kth_beg.next = next_end
        kth_end.next = next_beg
        return head
    else:  # case of swapping head and tail of the linked list
        # case for single element
        if size == 1:
            return
        second_last_node = getNthfromBeg(head, size - 1)  # get node previous to tail
        last_node = second_last_node.next  # get tail node
        last_node.next = head.next
        second_last_node.next = head
        head.next = None
        # a.head = last_node  # change the head to new head
        return last_node


# {
#  Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node


# returns the nth node from end.
def getNthfromEnd(head, n):
    # using two pointers, similar to finding middle element
    curr_node = head
    nth_node = head

    while n:
        if n and curr_node == None:
            return None
        curr_node = curr_node.next
        n -= 1

    while curr_node:
        curr_node = curr_node.next
        nth_node = nth_node.next

    return nth_node


# returns the nth node from beg.
def getNthfromBeg(head, n):
    curr_node = head
    for i in range(n - 1):
        if curr_node is None:
            return None
        else:
            curr_node = curr_node.next

    return curr_node


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n, kth_node = map(int, input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        # intial nodes at respective positions.
        check = [getNthfromBeg(a.head, kth_node), getNthfromEnd(a.head, kth_node)]

        new_head = swapkthnode(a.head, n, kth_node)

        new_check = [getNthfromEnd(new_head, kth_node), getNthfromBeg(new_head, kth_node)]
        if (check == new_check):
            print(1)
        else:
            print(0)
# } Driver Code Ends