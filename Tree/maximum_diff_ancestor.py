# User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

_MIN = -2147483648
_MAX = 2147483648


def maxDiffUtil(t, res):
    """ Returning Maximum value if node
    is not there (one child case) """
    if (t == None):
        return _MAX, res

    """ If leaf node then just return 
        node's value """
    if (t.left == None and t.right == None):
        return t.data, res

    """ Recursively calling left and right  
    subtree for minimum value """
    a, res = maxDiffUtil(t.left, res)
    b, res = maxDiffUtil(t.right, res)
    val = min(a, b)

    """ Updating res if (node value - minimum  
    value from subtree) is bigger than res """
    res = max(res, t.data - val)

    """ Returning minimum value got so far """
    return min(val, t.data), res


def maxDiff(root):
    '''
    :param root: Root of given tree
    :return: Integer
    '''
    res = _MIN
    x, res = maxDiffUtil(root, res)
    return res


# {
#  Driver Code Starts
# Initial Template for Python 3

# Contributed by Shivam Gupta
from collections import deque


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        print(maxDiff(root))

# } Driver Code Ends