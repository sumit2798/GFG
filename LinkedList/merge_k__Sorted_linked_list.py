# User function Template for python3

def MergeLists(n1, n2):
    ret = None

    # selecting node for making head
    # of merged list
    if n2.data < n1.data:
        ret = n2
        n2 = n2.next
    else:
        ret = n1
        n1 = n1.next

    tail = ret

    while n1 is not None and n2 is not None:
        # picking the smaller node
        if n2.data < n1.data:
            tail.next = n2
            tail = n2
            n2 = n2.next
        else:
            tail.next = n1
            tail = n1
            n1 = n1.next

    # adding the remaining list
    if n1:
        tail.next = n1
    if n2:
        tail.next = n2

    return ret


'''
The main function that takes an array of lists
arr[0..last] and generates the sorted output
'''


def mergeKLists(arr, N):
    last = N - 1
    # last index in array
    # repeat until only one list is left

    while last != 0:
        i = 0
        j = last
        # (i, j) forms a pair

        while i < j:
            # merge List i with List j and store
            # merged list in List i
            arr[i] = MergeLists(arr[i], arr[j])

            # consider next pair
            i += 1
            j -= 1

            # If all pairs are merged, update last
            if (i >= j):
                last = j

    return arr[0]


# {
#  Driver Code Starts

# Initial Template for Python 3

class Node:
    def __init__(self, x):
        self.data = x
        self.nxt = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, x):
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            self.tail.nxt = Node(x)
            self.tail = self.tail.nxt

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.nxt
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        line = [int(x) for x in input().strip().split()]
        heads = []
        index = 0
        for i in range(n):
            heads.append(LinkedList())
            size = line[index]
            for j in range(index + 1, index + 1 + size):
                heads[i].add(line[j])
            index += size + 1

        merged_list = merge(heads, n)
        merged_list.printList()

# } Driver Code Ends